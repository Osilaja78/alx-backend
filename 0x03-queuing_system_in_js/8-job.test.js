import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';


describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue({ redis: { port: 6379, host: '127.0.0.1', db: 3 } });
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw error if jobs is not array', () => {
    expect(() => createPushNotificationsJobs('random string', queue)).to.throw('Jobs is not an array');
  });

  it('should create job for each item in the jobs array', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
      { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('should attach event listeners to the created jobs', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
    ];

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];
    expect(job.listeners('enqueue')).to.have.lengthOf(1);
    expect(job.listeners('complete')).to.have.lengthOf(1);
    expect(job.listeners('failed')).to.have.lengthOf(1);
    expect(job.listeners('progress')).to.have.lengthOf(1);
  });
});
