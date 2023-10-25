# /usr/bin/env python3
""" FIFO caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """assign to the dictionary"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                print("DISCARD:", discard)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to the key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
