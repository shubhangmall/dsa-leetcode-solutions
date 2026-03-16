# [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

## Problem Description
Given an integer array `nums`, return the length of the longest **strictly increasing subsequence**.

A **subsequence** is a derivation from an array that can be formed by deleting some or no elements without changing the order of the remaining elements.

**Example:**
- **Input:** `nums = [10,9,2,5,3,7,101,18]`
- **Output:** `4`
- **Explanation:** The longest increasing subsequence is `[2,3,7,101]`, therefore the length is `4`.

## Intuition
This approach uses **Bottom-Up Dynamic Programming**. Instead of trying to find the global maximum immediately, we solve the subproblem: "What is the longest increasing subsequence that *starts* at index `i`?"

**The Strategy:**
1.  **DP Array Initialization:** Create an array `LIS` where `LIS[i]` represents the length of the longest increasing subsequence starting at index `i`. Every element is initialized to `1` because a single number is a valid subsequence of length 1.
2.  **Right-to-Left Traversal:** By iterating backward from the end of the array, we ensure that when we are at index `i`, we already know the optimal solutions for all elements to its right.
3.  **Nested Comparison:** For each element at index `i`, we look at every element `j` to its right:
    * If `nums[i] < nums[j]`, then `nums[i]` can be placed before the subsequence starting at `j`.
    * We update `LIS[i]` to be the maximum of its current value or `1 + LIS[j]`.
4.  **Final Result:** The longest increasing subsequence in the entire array is simply the maximum value stored in our `LIS` array.

## Complexity
- **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`. We use two nested loops: the outer loop runs $n$ times, and the inner loop runs up to $n$ times.
- **Space Complexity:** $O(n)$ to store the `LIS` array which keeps track of the longest subsequence length for each index.