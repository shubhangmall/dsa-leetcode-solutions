from collections import defaultdict, OrderedDict

class LFUCache:
    # time: O(1) — all operations use hashmaps and OrderedDict which are O(1)
    # space: O(capacity) — storing at most capacity elements across all hashmaps
    def __init__(self, capacity: int):
        # store the maximum capacity of the cache
        self.capacity = capacity
        # track the minimum frequency of any key in the cache
        self.min_freq = 0
        # hashmap storing key to its value
        self.key_to_val = {}
        # hashmap storing key to its access frequency
        self.key_to_freq = {}
        # hashmap storing frequency to ordered dict of keys at that frequency
        self.freq_to_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        # return -1 if key does not exist in cache
        if key not in self.key_to_val:
            return -1
        # increment frequency of accessed key
        self._increment_freq(key)
        # return the value of the key
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        # do nothing if capacity is zero
        if self.capacity == 0:
            return
        # if key already exists update its value and increment frequency
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._increment_freq(key)
        else:
            # if cache is full evict the least frequently used key
            if len(self.key_to_val) == self.capacity:
                # remove oldest key at minimum frequency bucket
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                # remove evicted key from value map
                del self.key_to_val[evict_key]
                # remove evicted key from frequency map
                del self.key_to_freq[evict_key]
            # insert new key with its value
            self.key_to_val[key] = value
            # new key always starts with frequency 1
            self.key_to_freq[key] = 1
            # add new key to frequency 1 bucket
            self.freq_to_keys[1][key] = None
            # new key has frequency 1 so min frequency resets to 1
            self.min_freq = 1

    def _increment_freq(self, key: int) -> None:
        # get current frequency of key
        freq = self.key_to_freq[key]
        # remove key from its current frequency bucket
        del self.freq_to_keys[freq][key]
        # if current min frequency bucket is now empty increment min frequency
        if not self.freq_to_keys[self.min_freq]:
            self.min_freq += 1
        # update key frequency to next frequency
        self.key_to_freq[key] = freq + 1
        # add key to next frequency bucket
        self.freq_to_keys[freq + 1][key] = None