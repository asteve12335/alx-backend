#!/usr/bin/python3
""" LFU Caching """


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ A class LFUCache that inherits
    from BaseCaching and is a caching system """

    def __init__(self):
        """ Initialize LFUCache """
        super().__init__()
        self.lfu = {}
        self.lfu_counter = 0

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lfu[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    min_key = min(self.lfu, key=self.lfu.get)
                    self.cache_data.pop(min_key)
                    self.lfu.pop(min_key)
                    print("DISCARD: {}".format(min_key))
                self.cache_data[key] = item
                self.lfu[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.lfu[key] += 1
        return self.cache_data[key]
