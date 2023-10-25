#!/usr/bin/python3
""" A module BasicCache that inherits
from BaseCaching and is a caching system """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ A class BasicCache that inherits
    from BaseCaching and is a caching system """

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
