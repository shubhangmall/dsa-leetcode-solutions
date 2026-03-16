# [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/)

## Problem Description
Given an integer array `nums` and an integer `k`, return the number of **good subarrays** of `nums`.

A **good subarray** is an array where the number of different integers in that array is exactly `k`.

**Example:**
- **Input:** `nums = [1,2,1,2,3], k = 2`
- **Output:** `7`
- **Explanation:** Subarrays formed with exactly 2 different integers: `[1,2]`, `[1,2,1]`, `[1,2,1,2]`, `[2,1]`, `[2,1,2]`, `[1,2]`, `[2,3]`.

## Intuition
The problem asks for subarrays with **exactly** `k` distinct elements. Finding "exactly" is often harder than finding "at most." 

A key observation in sliding window problems is that:
`Exactly(k) = AtMost(k) - AtMost(k - 1)`

By solving the helper problem "count the number of subarrays with **at most** `k` distinct elements," we can easily derive the answer.

**The Strategy (AtMost Helper):**
1.  Use a **Sliding Window** with two pointers, `left` and `right`.
2.  Maintain a frequency map (Hash Map) of the elements currently in the window.
3.  Expand the `right` pointer to include a new number.
4.  If the number of distinct elements in the map exceeds `k`, shrink the window from the `left` until the count of distinct elements is `k` or less.
5.  At each step, the number of subarrays ending at `right` that have at most `k` distinct elements is `right - left + 1`. Add this to your total.



## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the length of `nums`. We run the "at most" helper function twice. In each run, the `left` and `right` pointers each travel from $0$ to $n$ exactly once.
- **Space Complexity:** $O(k)$, as the frequency map will store at most $k + 1$ distinct elements at any given time.