#!/usr/bin/env python3
"""100-lfu_cache.py module"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    A caching class that follows the LFU rule,
    it inherits from BaseCaching.
    """

    def __init__(self):
        """Initializatioin method"""

        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Assign to the dictionary self.cache_data"""

        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        elif len(self.cache_data) >= self.MAX_ITEMS:
            min_frequency = min(self.frequency.values())
            lfu_keys = [
                k for k, v in self.frequency.items() if v == min_frequency
            ]

            if len(lfu_keys) > 1:
                lru_key = min(self.cache_data, key=self.frequency.get)
                lfu_keys.remove(lru_key)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            lfu_key = lfu_keys[0]
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            print(f"DISCARD: {lfu_key}")

        self.cache_data[key] = item
        self.frequency[key] = 1

    def get(self, key):
        """
        Return the value of key in self.cache_data,
        or None if key does not exits.
        """

        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        else:
            return None
