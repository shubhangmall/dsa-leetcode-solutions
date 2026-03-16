# [460. LFU Cache](https://leetcode.com/problems/lfu-cache/)

## Problem Description
Design and implement a data structure for a **Least Frequently Used (LFU)** cache.

Implement the `LFUCache` class:
* `LFUCache(int capacity)` Initializes the object with the `capacity` of the data structure.
* `int get(int key)` Gets the value of the `key` if the `key` exists in the cache. Otherwise, returns `-1`.
* `void put(int key, int value)` Update the value of the `key` if present, or inserts the `key` if not already present. When the cache reaches its `capacity`, it should invalidate and remove the **least frequently used** key before inserting a new item. For this problem, when there is a **tie** (i.e., two or more keys with the same frequency), the **least recently used (LRU)** key would be invalidated.

To determine the least frequently used key, a **use counter** is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

## Intuition
To achieve $O(1)$ time complexity for both `get` and `put`, we need a way to track both the **frequency** of access and the **recency** of access within each frequency group.

**The Strategy:**
1.  **Frequency Mapping:** We use a Hash Map where the key is the `frequency` and the value is a **Doubly Linked List** (or an `OrderedDict` in Python). This list stores all keys that have been accessed that specific number of times.
2.  **LRU within LFU:** Within each frequency's Doubly Linked List, we maintain elements in LRU order. The most recently accessed key is moved to the front/end, and the least recently used is at the tail/start.
3.  **Key Tracking:** A second Hash Map stores the actual `key -> (value, frequency)` and a reference to the node in the linked list for $O(1)$ access.
4.  **Min Frequency Tracker:** We keep an integer `min_freq` to track the current lowest frequency in the cache. When we need to evict an item, we go to `frequency_map[min_freq]` and remove the least recently used node.
5.  **Promotion:** Whenever a key is accessed (`get`) or updated (`put`), its frequency increases. We move it from its current frequency list to the `frequency + 1` list. If the old list becomes empty and it was the `min_freq`, we increment `min_freq`.

## Complexity
- **Time Complexity:** $O(1)$ for both `get` and `put` operations. By using hash maps combined with doubly linked lists, we can add, remove, and update elements in constant time.
- **Space Complexity:** $O(capacity)$, as we store at most the given capacity number of keys in our hash maps and linked lists.