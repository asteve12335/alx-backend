#!/usr/bin/python3
""" FIFO Caching """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A class FIFOCache that inherits
    from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()
        self.fifo = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.fifo.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.cache_data.pop(self.fifo[0])
                    print("DISCARD: {}".format(self.fifo[0]))
                    self.fifo.pop(0)
                self.cache_data[key] = item
            self.fifo.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
