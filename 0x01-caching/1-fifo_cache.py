#!/usr/bin/env python3
"""1-fifo_cache.py module"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    A caching class that follows the FIFO rule,
    it inherits from BaseCaching.
    """

    def __init__(self):
        """Initializatioin method"""

        super().__init__()
        self.queue = OrderedDict()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data"""

        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key, _ = self.queue.popitem(last=False)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.queue[key] = True

    def get(self, key):
        """
        Return the value of key in self.cache_data,
        or None if key does not exits.
        """

        value = self.cache_data.get(key)

        if key or value is not None:
            return value
        return None
