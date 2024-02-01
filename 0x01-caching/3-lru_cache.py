#!/usr/bin/env python3
"""3-lru_cache.py module"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A caching class that follows the LRU rule,
    it inherits from BaseCaching.
    """

    def __init__(self):
        """Initializatioin method"""

        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data"""

        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    lru_key = self.order.pop(0)
                    del self.cache_data[lru_key]
                    print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """
        Return the value of key in self.cache_data,
        or None if key does not exits.
        """

        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        else:
            return None
