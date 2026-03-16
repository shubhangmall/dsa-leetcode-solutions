# [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)

## Problem Description
Given an `m x n` `matrix`, return all elements of the `matrix` in **spiral order**.

**Example:**
- **Input:** `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- **Output:** `[1,2,3,6,9,8,7,4,5]`

## Intuition
To traverse the matrix in a spiral, we can define four boundaries: `top`, `bottom`, `left`, and `right`. We simulate the path of a traveler moving in a cycle:
1. **Move Right:** Traverse from `left` to `right` along the `top` row, then increment `top`.
2. **Move Down:** Traverse from `top` to `bottom` along the `right` column, then decrement `right`.
3. **Move Left:** Traverse from `right` to `left` along the `bottom` row (if `top <= bottom`), then decrement `bottom`.
4. **Move Up:** Traverse from `bottom` to `top` along the `left` column (if `left <= right`), then increment `left`.

We continue this process until the boundaries cross each other.



## Complexity
- **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. Every element in the matrix is visited exactly once.
- **Space Complexity:** $O(1)$ (ignoring the space required for the output list), as we only use a few variables to track the boundaries.