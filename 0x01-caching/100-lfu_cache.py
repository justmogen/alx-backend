#!/usr/bin/env python3
""" LFU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class with LRU algorithm"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.queue = []
        self.count = {}

    def put(self, key, item):
        """remove least frequently used eleement """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
                self.queue.append(key)
                self.count[key] += 1
                return
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop(0)
                del self.cache_data[discard]
                del self.count[discard]
                print("DISCARD:", discard)
            self.queue.append(key)
            self.cache_data[key] = item
            self.count[key] = 1

    def get(self, key):
        """return the value linked to the key"""
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            self.count[key] += 1
            return self.cache_data[key]
        return None
