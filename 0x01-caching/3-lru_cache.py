#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ A class LRUCache that inherits
    from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.lru = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lru.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.cache_data.pop(self.lru[0])
                    print("DISCARD: {}".format(self.lru[0]))
                    self.lru.pop(0)
                self.cache_data[key] = item
            self.lru.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.lru.remove(key)
        self.lru.append(key)
        return self.cache_data[key]
