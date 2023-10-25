#!/usr/bin/env python3
""" LFU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class with LFU algorithm"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.frequencies = {}  # Dictionary to store frequencies of keys

    def put(self, key, item):
        """add an item in cache with LFU eviction policy"""
        if key and item:
            if key in self.cache_data:
                # Update the item and frequency
                self.cache_data[key] = item
                self.frequencies[key] += 1
            else:
                # Add the new item and set its frequency to 1
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Evict the least frequently used item(s)
                    min_frequency = min(self.frequencies.values())
                    keys_to_remove = [
                        k for k, v in self.frequencies.items()
                        if v == min_frequency]
                    # Remove the first item that was least frequently used
                    discard = keys_to_remove[0]
                    del self.cache_data[discard]
                    del self.frequencies[discard]
                    print("DISCARD:", discard)
                self.cache_data[key] = item
                self.frequencies[key] = 1

    def get(self, key):
        """return the value linked to key"""
        if key in self.cache_data:
            # Update the frequency
            self.frequencies[key] += 1
            return self.cache_data[key]
        return None

    def cache_info(self):
        """return cache information"""
        return self.cache_data, self.frequencies
