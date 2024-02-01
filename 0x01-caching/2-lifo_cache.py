#!/usr/bin/env python3
"""2-lifo_cache.py module"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching class that follows the LIFO rule,
    it inherits from BaseCaching.
    """

    def __init__(self):
        """Initializatioin method"""

        super().__init__()
        self.last_added = ''

    def put(self, key, item):
        """Assign to the dictionary self.cache_data"""

        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    print(f"DISCARD: {self.last_added}")
                    del self.cache_data[self.last_added]

            self.last_added = key
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value of key in self.cache_data,
        or None if key does not exits.
        """

        value = self.cache_data.get(key)

        if key or value is not None:
            return value
        return None
