#!/usr/bin/env python3
""" MRU Caching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """remove most recently used eleement """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop()
                del self.cache_data[discard]
                print("DISCARD:", discard)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to the key"""
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
