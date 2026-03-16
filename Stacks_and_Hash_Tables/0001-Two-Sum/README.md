# [1. Two Sum](https://leetcode.com/problems/two-sum/)

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example:**
- Input: `nums = [2,7,11,15], target = 9`
- Output: `[0,1]` (Because `nums[0] + nums[1] == 9`)

## Intuition
A brute-force nested loop takes $O(n^2)$. By using a **Hash Map**, we can store each number's value and its index as we iterate. For each element, we check if its "complement" (`target - current_value`) already exists in the map. This trades space for a significant boost in speed.

## Complexity
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$