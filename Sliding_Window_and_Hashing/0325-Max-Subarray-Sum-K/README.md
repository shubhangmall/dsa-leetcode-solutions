# [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)

## Problem Description
Given an integer array `nums` and an integer `k`, return the **maximum length** of a subarray that sums to `k`. If there is not one, return `0` instead.

**Example:**
- **Input:** `nums = [1, -1, 5, -2, 3], k = 3`
- **Output:** `4` (The subarray `[1, -1, 5, -2]` sums to 3 and has length 4)
- **Input:** `nums = [-2, -1, 2, 1], k = 1`
- **Output:** `2` (The subarray `[-1, 2]` sums to 1 and has length 2)

## Intuition
The problem asks for a subarray sum, which strongly suggests using **Prefix Sums**. A subarray sum from index `i` to `j` can be calculated as:
$Sum(i, j) = PrefixSum[j] - PrefixSum[i-1]$

We are looking for a case where $PrefixSum[j] - PrefixSum[i-1] = k$. Rearranging this, we get:
$PrefixSum[i-1] = PrefixSum[j] - k$



**The Strategy:**
1. Maintain a running `current_sum` (Prefix Sum) as we iterate through the array.
2. Use a **Hash Map** to store the *first* time we encounter a specific prefix sum (`{sum: index}`).
3. For each element at index `j`, calculate `target = current_sum - k`.
4. If `target` exists in our map, it means the subarray from `map[target] + 1` to `j` sums to `k`.
5. Calculate the length (`j - map[target]`) and update the maximum.
6. **Note:** Initialize the map with `{0: -1}` to handle cases where the subarray starts from index 0.

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the number of elements in `nums`. We traverse the array once, performing $O(1)$ map lookups.
- **Space Complexity:** $O(n)$, as in the worst case, we store every prefix sum in the Hash Map.