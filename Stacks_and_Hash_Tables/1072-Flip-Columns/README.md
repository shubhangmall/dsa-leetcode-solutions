# [1072. Flip Columns For Maximum Number of Equal Rows](https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/)

## Problem Description
You are given an `m x n` binary matrix `matrix`. You can choose any number of columns and flip every cell in that column (0 becomes 1, and 1 becomes 0).

Return the **maximum number of rows** that have all values equal after some number of flips.

**Example:**
- **Input:** `matrix = [[0,1],[1,1]]`
- **Output:** `1` (After flipping the first column, the rows become `[1,1]` and `[0,1]`. Only one row is equal.)
- **Input:** `matrix = [[0,0,0],[0,0,1],[1,1,0]]`
- **Output:** `2` (After flipping the last column, rows 1 and 3 become all 0s or all 1s.)

## Intuition
At first glance, this looks like a complex optimization problem. However, the core observation is: 
Two rows can be made identical (all 0s or all 1s) if and only if:
1. They are already **identical** (e.g., `010` and `010`).
2. They are **exact opposites** (e.g., `010` and `101`).

If two rows fit this criteria, any column flip that makes one row all 0s or all 1s will do the same for the other. Therefore, the problem reduces to finding the most frequent "pattern" or its "inverse" in the matrix.

**The Trick:** For each row, if it starts with a `1`, flip the whole row to start with `0`. This "normalizes" the row. Now, all rows that were either identical or opposites will have the exact same normalized string representation. We just need to count which normalized string appears most often.



## Complexity
- **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns, as we must process every cell to create the row patterns.
- **Space Complexity:** $O(m \cdot n)$ in the worst case to store the row patterns in a Hash Map.