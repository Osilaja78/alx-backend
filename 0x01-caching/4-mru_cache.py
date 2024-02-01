#!/usr/bin/env python3
"""4-mru_cache.py module"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    A caching class that follows the MRU rule,
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
                    mru_key = self.order.pop()
                    del self.cache_data[mru_key]
                    print(f"DISCARD: {mru_key}")

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
