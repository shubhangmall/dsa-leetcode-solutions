# [2163. Minimum Difference in Sums After Removal of Elements](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/)

## Problem Description
You are given a **0-indexed** integer array `nums` consisting of `3 * n` elements.

You must remove exactly `n` elements from `nums` to leave `2 * n` elements. The remaining elements are split into two parts:
1.  The first `n` elements form the **first part**.
2.  The second `n` elements form the **second part**.

The **difference** is calculated as `sum(first_part) - sum(second_part)`. Return the **minimum possible difference** after removing exactly `n` elements.

**Example:**
- **Input:** `nums = [3,1,2]` ($n=1$)
- **Output:** `-1`
- **Explanation:** We must remove 1 element.
  - Remove `nums[1]`: `[3, 2]`. Diff = $3 - 2 = 1$.
  - Remove `nums[2]`: `[3, 1]`. Diff = $3 - 1 = 2$.
  - Remove `nums[0]`: `[1, 2]`. Diff = $1 - 2 = -1$.
  - Min difference is `-1`.

## Intuition
To minimize the difference `sum(first) - sum(second)`, we need to:
1.  **Minimize the sum of the first part.**
2.  **Maximize the sum of the second part.**

Since we must leave $n$ elements in each part from a total of $3n$, there is a "split point" $i$ that can range from index $n$ to $2n$. For any chosen split point $i$, the first part is formed by the smallest $n$ elements from `nums[0...i-1]`, and the second part is formed by the largest $n$ elements from `nums[i...3n-1]`.

**The Strategy:**
1.  **Prefix Minimum Sums:** Use a **Max-Heap** to keep track of the $n$ smallest elements as you iterate from index $0$ to $2n-1$. At each index $i \ge n-1$, store the current sum of these $n$ smallest elements in a `min_prefix_sum` array.
2.  **Suffix Maximum Sums:** Use a **Min-Heap** to keep track of the $n$ largest elements as you iterate backwards from index $3n-1$ down to $n$. Store the current sum of these $n$ largest elements in a `max_suffix_sum` array.
3.  **Find the Optimal Split:** Iterate through all possible split points $i$ (where $i$ ranges from $n$ to $2n$) and calculate `min_prefix_sum[i-1] - max_suffix_sum[i]`. The minimum of these values is our answer.



## Complexity
- **Time Complexity:** $O(n \log n)$, where $n$ is $1/3$ the length of the input array. We perform two passes across the array (forward and backward), each using a heap of size $n$ to maintain the smallest/largest elements.
- **Space Complexity:** $O(n)$ to store the `min_prefix_sum` and `max_suffix_sum` arrays, as well as the heaps.