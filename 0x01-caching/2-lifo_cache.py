# /usr/bin/env python3
""" LIFO caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """remove last element if full and put new item from down"""
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop()
                del self.cache_data[discard]
                print("DISCARD:", discard)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to the key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
