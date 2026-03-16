# [3369. Design an Array Statistics Tracker](https://leetcode.com/problems/design-an-array-statistics-tracker/)

## Problem Description
Design a data structure that maintains a dynamic collection of numbers and supports efficient updates and statistical queries.

Implement the `StatisticsTracker` class:
* `StatisticsTracker()`: Initializes the tracker.
* `void addNumber(int number)`: Adds `number` to the tracker.
* `void removeFirstAddedNumber()`: Removes the earliest added number (FIFO).
* `int getMean()`: Returns the floored mean of all current numbers.
* `int getMedian()`: Returns the median. If there are two middle values, return the larger one.
* `int getMode()`: Returns the most frequent value. If there's a tie, return the smallest value.

## Intuition
This problem requires balancing multiple data structures to keep all operations efficient (mostly $O(1)$ or $O(\log N)$). Because we need to remove the "first added" element, a **Queue** is necessary for tracking insertion order.

**The Strategy:**
1.  **Mean:** Maintain a running `total_sum` and a `count`. The mean is simply `total_sum // count`.
2.  **Median:** We need the middle element of a sorted version of our numbers. A **Sorted List** (or two balanced heaps/balanced BST) allows us to add/remove elements in $O(\log N)$ and access the middle element in $O(1)$ or $O(\log N)$.
3.  **Mode:** We need to track frequencies.
    * Use a **Hash Map** (`count`) to store `number -> frequency`.
    * Use a **Max-Heap** or a second **Sorted List** to store `(frequency, -number)`. This allows us to quickly find the highest frequency and use the smallest number as a tie-breaker.
    * When removing a number, we don't necessarily need to remove it from the heap immediately (which is slow). We can use **Lazy Removal**: only pop from the heap when `getMode()` is called if the top element's frequency no longer matches our Hash Map.



## Complexity
- **Time Complexity:**
    * `addNumber`: $O(\log N)$ to update the sorted list and frequency structures.
    * `removeFirstAddedNumber`: $O(\log N)$ to remove from the sorted list.
    * `getMean`: $O(1)$.
    * `getMedian`: $O(1)$ with a indexed sorted list.
    * `getMode`: Amortized $O(\log N)$ due to lazy heap removals.
- **Space Complexity:** $O(N)$ to store the numbers in the queue, sorted list, and frequency map.