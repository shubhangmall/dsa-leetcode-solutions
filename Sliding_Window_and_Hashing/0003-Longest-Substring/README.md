# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem Description
Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example:**
- **Input:** `s = "abcabcbb"`
- **Output:** `3` (The longest substring is "abc")
- **Input:** `s = "bbbbb"`
- **Output:** `1` (The longest substring is "b")

## Intuition
The most efficient way to solve this is using a **Sliding Window** with two pointers (`left` and `right`) and a **Hash Map** (or Hash Set):
1. Use the `right` pointer to expand the window by adding characters one by one.
2. Use a Hash Map to store the last seen index of each character.
3. If the character at `right` is already in the map and its index is within the current window, move the `left` pointer to `index + 1` to "slide" past the duplicate.
4. At each step, calculate the window size (`right - left + 1`) and update the maximum length found so far.

By jumping the `left` pointer directly to the necessary position using the map, we avoid unnecessary re-scanning of the string.

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the length of the string. Each character is visited at most twice (once by each pointer).
- **Space Complexity:** $O(min(m, n))$, where $m$ is the size of the character set (e.g., 26 for English letters, or more for ASCII/Unicode). We store character positions in a Hash Map.