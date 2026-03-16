# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

## Problem Description
Roman numerals are represented by seven different symbols: `I, V, X, L, C, D` and `M`. Given a roman numeral, convert it to an integer.

**Example:**
- Input: `s = "MCMXCIV"`
- Output: `1994` (M = 1000, CM = 900, XC = 90, IV = 4)

## Intuition
We map each Roman symbol to its value. We iterate through the string from left to right. If the current symbol's value is smaller than the next symbol's value (like `I` before `V`), we subtract it. Otherwise, we add it.

## Complexity
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$