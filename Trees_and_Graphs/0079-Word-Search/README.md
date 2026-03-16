# [79. Word Search](https://leetcode.com/problems/word-search/)

## Problem Description
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

**Example:**
- **Input:** `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"`
- **Output:** `true`

## Intuition
To solve this, we use **Backtracking** via Depth-First Search (DFS) to explore all possible paths that could form the target word.

**The Strategy:**
1.  **Iterative Start:** We loop through every cell in the grid. If a cell matches the first character of the word, we initiate a `dfs`.
2.  **Recursive Exploration:** Our `dfs` function checks the current character and moves to adjacent cells (up, down, left, right).
3.  **Path Tracking:** To ensure we don't reuse the same cell in a single path, we maintain a `path` set. 
    * Before moving to the next character, we **add** the current `(row, col)` to the set.
    * After exploring all four directions from that cell, we **remove** (backtrack) the current `(row, col)` so it can be used in other potential paths.
4.  **Base Cases:**
    * **Success:** If `word_idx` equals the length of the word, we've successfully matched every character.
    * **Failure:** If we go out of bounds, hit a character that doesn't match, or revisit a cell already in our current `path`, we stop that branch of exploration.



## Complexity
- **Time Complexity:** $O(M \cdot N \cdot 4^L)$, where $M \times N$ is the board size and $L$ is the length of the word. For each of the $M \cdot N$ starting cells, we explore up to 4 directions at each step for the length of the word.
- **Space Complexity:** $O(L)$, representing the maximum depth of the recursion stack and the maximum size of the `path` set, which are both bounded by the length of the word.