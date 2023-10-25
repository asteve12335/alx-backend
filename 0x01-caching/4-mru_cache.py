#!/usr/bin/python3
""" MRU Caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ A class MRUCache that inherits
    from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.mru.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.cache_data.pop(self.mru[-1])
                    print("DISCARD: {}".format(self.mru[-1]))
                    self.mru.pop(-1)
                self.cache_data[key] = item
            self.mru.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.mru.remove(key)
        self.mru.append(key)
        return self.cache_data[key]
