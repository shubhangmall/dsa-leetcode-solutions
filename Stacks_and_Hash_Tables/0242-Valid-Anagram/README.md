# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example:**
- Input: `s = "anagram", t = "nagaram"`
- Output: `true`

## Intuition
We use a **Frequency Counter** (Hash Map). We increment counts for characters in the first string and decrement for the second. If the strings are of different lengths or any count in our map is non-zero at the end, they are not anagrams.

## Complexity
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$ (The space is bounded by the size of the alphabet, e.g., 26 characters).