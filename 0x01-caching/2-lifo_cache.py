#!/usr/bin/python3
""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A class LIFOCache that inherits
    from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize LIFOCache """
        super().__init__()
        self.lifo = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lifo.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.cache_data.pop(self.lifo[-1])
                    print("DISCARD: {}".format(self.lifo[-1]))
                    self.lifo.pop(-1)
                self.cache_data[key] = item
            self.lifo.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
