#!/usr/bin/env python3
"""inherit from base_caching to implement pu() and get() methods"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class"""

    def put(self, key, item):
        """assign to the dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value linked to the key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
