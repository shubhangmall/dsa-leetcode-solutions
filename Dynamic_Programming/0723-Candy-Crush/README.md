# [723. Candy Crush](https://leetcode.com/problems/candy-crush/)

## Problem Description
This problem simulates a basic version of the game Candy Crush. Given a 2D integer array `board` representing the grid of candies, different positive integers represent different types of candies. A value of `0` represents an empty cell.

You need to implement a function to "crush" candies according to these rules:
1.  **Crush:** If three or more candies of the same type are adjacent vertically or horizontally, they should all be crushed simultaneously by setting their values to `0`.
2.  **Drop:** After crushing, candies above the empty spaces should drop down to fill the gaps.
3.  **Repeat:** This process continues until no more candies can be crushed.

Return the final state of the board.

**Example:**
- **Input:** `board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],...]`
- **Output:** The board state after all stable drops are completed.

## Intuition
The problem is best solved by breaking it down into three distinct phases that repeat in a loop until the board becomes stable (no more crushes occur).

**The Strategy:**
1.  **Identify (Marking):**
    * Iterate through the board to find three or more consecutive identical candies horizontally and vertically.
    * Instead of setting them to `0` immediately (which would ruin the check for other candies), mark them (e.g., by making the value negative: `board[r][c] = -abs(board[r][c])`).
    * This ensures that a candy can part of both a horizontal and vertical crush simultaneously.

2.  **Crush & Drop (Gravity):**
    * Iterate through each column. 
    * Use a "two-pointer" or "read-write" approach to move all positive candies (non-crushed) to the bottom of the column.
    * Fill the remaining top cells of the column with `0`.

3.  **Repeat:**
    * If any candies were marked in step 1, the board was not stable. Repeat the entire process.
    * If no candies were marked, the board is stable; return the board.



## Complexity
- **Time Complexity:** $O((R \cdot C)^2)$, where $R$ is the number of rows and $C$ is the number of columns. In each iteration, we scan the entire board $O(R \cdot C)$. In the worst case, only a few candies are crushed per iteration, leading to multiple passes.
- **Space Complexity:** $O(1)$ if we mark the board in-place (using negative values), or $O(R \cdot C)$ if we use a separate boolean array to keep track of crushed candies.