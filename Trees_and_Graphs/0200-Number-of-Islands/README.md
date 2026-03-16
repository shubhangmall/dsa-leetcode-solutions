# [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

## Problem Description
Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the **number of islands**.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example:**
- **Input:** grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
- **Output:** `3`

## Intuition
This is a classic graph traversal problem. We can treat the 2D grid as an undirected graph where each `'1'` is a node, and edges connect adjacent `'1'`s (up, down, left, right). 

To find the number of connected components (islands):
1. Iterate through every cell in the grid using nested loops.
2. When we encounter a `'1'` (land), it means we've found a new island. We immediately increment our island counter.
3. To ensure we don't count this same island again later, we trigger a **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** starting from that cell.
4. During the traversal, we visit all connected land cells and "sink" them by changing the `'1'`s to `'0'`s. 



## Complexity
- **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. We iterate through every cell in the grid, and the DFS/BFS visits each cell at most once.
- **Space Complexity:** $O(m \cdot n)$ in the worst case. If the entire grid is filled with `'1'`s (a single giant island), the DFS recursion stack will go $m \cdot n$ levels deep.