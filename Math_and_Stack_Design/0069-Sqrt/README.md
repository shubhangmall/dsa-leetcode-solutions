# [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)

## Problem Description
Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator (e.g., `pow(x, 0.5)` or `x ** 0.5`).

**Example:**
- **Input:** `x = 8`
- **Output:** `2` (The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.)

## Intuition
The square root of `x` must lie between `0` and `x`. Since the range is sorted, we can use **Binary Search** to efficiently find the largest integer $k$ such that $k^2 \le x$.



**The Strategy:**
1.  Initialize `left = 0` and `right = x`.
2.  While `left <= right`, calculate the middle point `mid`.
3.  If $mid^2 = x$, then `mid` is the exact square root.
4.  If $mid^2 < x$, then `mid` could be the answer, so we store it and search the right half (`left = mid + 1`) to see if there is a larger valid integer.
5.  If $mid^2 > x$, the square root must be smaller, so we search the left half (`right = mid - 1`).

*Tip: To avoid integer overflow in languages like C++ or Java, use $mid = x // mid$ for comparison instead of $mid \cdot mid = x$.*

## Complexity
- **Time Complexity:** $O(\log x)$, because we are halving the search space in each step of the binary search.
- **Space Complexity:** $O(1)$, as we only use a few variables for the pointers and the result.