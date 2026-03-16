# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Problem Description
Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

**Example:**
- Input: `nums = [1,1,2]`
- Output: `2, nums = [1,2,_]` (The first two elements of nums being 1 and 2)

## Intuition
Since the array is already sorted, all duplicate elements will be adjacent to each other. We can use a **Two-Pointer approach**:
1. One pointer (`i`) keeps track of the position of the last unique element found.
2. A second pointer (`j`) iterates through the array to find new unique elements.
Whenever `nums[j]` is different from `nums[i]`, we increment `i` and update `nums[i]` with the value of `nums[j]`.

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the length of the array, as we iterate through the list once.
- **Space Complexity:** $O(1)$, because we modify the array in-place without using extra space for another data structure.