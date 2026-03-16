# [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

## Problem Description
You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order. The final sorted array should not be returned by the function, but instead be **stored inside the array `nums1`**. To accommodate this, `nums1` has a length of $m + n$.

**Example:**
- Input: `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`
- Output: `[1,2,2,3,5,6]`

## Intuition
The standard approach of merging from the beginning would require shifting elements in `nums1`, leading to $O(m \cdot n)$ complexity. To achieve optimal efficiency, we use a **Three-Pointer approach** starting from the **end** of the arrays:
1. Pointer `p1` at index $m - 1$ (last valid element in `nums1`).
2. Pointer `p2` at index $n - 1$ (last element in `nums2`).
3. Pointer `p` at index $m + n - 1$ (last slot in `nums1`).

By comparing the largest elements and placing them at the back, we ensure that we never overwrite an element in `nums1` before it has been processed.



## Complexity
- **Time Complexity:** $O(m + n)$, as we traverse each element in both arrays at most once.
- **Space Complexity:** $O(1)$, since the merge happens in-place within the existing capacity of `nums1`.