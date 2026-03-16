# [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## Problem Description
Implement the `RandomizedSet` class:
* `bool insert(int val)`: Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
* `bool remove(int val)`: Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
* `int getRandom()`: Returns a random element from the current set of elements. Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average $O(1)$** time complexity.

**Example:**
- `insert(1)`, `remove(2)`, `insert(2)`, `getRandom()`, `remove(1)`, `insert(2)`, `getRandom()`

## Intuition
The challenge is achieving $O(1)$ for both **deletion** and **random access**. 
1.  A **Hash Map** provides $O(1)$ insertion and deletion, but it doesn't support $O(1)$ random access (you can't easily pick a random key).
2.  An **Array (List)** provides $O(1)$ random access (via index), but deleting an arbitrary element is $O(n)$ because you have to shift elements.

**The Solution:** Use both!
- Use a **List** to store the actual values (for `getRandom`).
- Use a **Hash Map** to store `{value: index_in_list}` (for $O(1)$ lookup).

**The "Swap and Pop" Trick for Deletion:**
To delete an element in $O(1)$ without shifting:
1.  Find the index of the element to delete from the Map.
2.  Swap that element with the **last element** in the List.
3.  Update the Map with the new index of the swapped element.
4.  Pop the last element from the List.



## Complexity
- **Time Complexity:** Average $O(1)$ for all operations.
- **Space Complexity:** $O(n)$, where $n$ is the number of elements stored, to maintain both the List and the Hash Map.