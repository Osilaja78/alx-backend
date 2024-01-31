#!/usr/bin/env python3
"""0-basic_cache.py module"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching.
    Does not hav limit.
    """

    def put(self, key, item):
        """Assign to the dictionary self.cache_data"""

        if key and item:
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
