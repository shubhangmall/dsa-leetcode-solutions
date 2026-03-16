# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Problem Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example:**
- Input: `s = "()[]{}"`
- Output: `true`

## Intuition
This is a classic **Stack** problem. As we encounter opening brackets, we push them onto the stack. When we see a closing bracket, it must match the top of the stack. If the stack is empty or the brackets don't match, the string is invalid. 



## Complexity
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$