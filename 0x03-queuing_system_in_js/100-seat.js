const express = require('express');
const kue = require('kue');
const redis = require('redis');
const { promisify } = require('util');


const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);


const queue = kue.createQueue();


async function reserveSeat(number) {
  await setAsync('available_seats', number);
}


async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats) : 0;
}


reserveSeat(50);

let reservationEnabled = true;


const app = express();
const port = 1245;


app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});


app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
  } else {
    const job = queue.create('reserve_seat').save(err => {
      if (err) {
        res.json({ status: 'Reservation failed' });
      } else {
        res.json({ status: 'Reservation in process' });
      }
    });
  }
});


app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });
  const currentSeats = await getCurrentAvailableSeats();
  if (currentSeats === 0) {
    reservationEnabled = false;
  }
  const job = queue.process('reserve_seat', async (job, done) => {
    const seats = await getCurrentAvailableSeats();
    if (seats > 0) {
      await reserveSeat(seats - 1);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});


queue.on('job complete', (id) => {
  console.log(`Seat reservation job ${id} completed`);
});


queue.on('job failed', (id, err) => {
  console.log(`Seat reservation job ${id} failed: ${err}`);
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
