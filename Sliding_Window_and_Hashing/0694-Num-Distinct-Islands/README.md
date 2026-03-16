# [694. Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/)

## Problem Description
Given an `m x n` 2D binary grid `grid` which represents a map of `1`s (land) and `0`s (water), return the number of **distinct** islands. 

An island is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water. Two islands are considered to be the same if and only if one island can be translated (not rotated or reflected) to equal the other.

**Example:**
- **Input:** grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
  ]
- **Output:** `1` (The two 2x2 square islands are identical in shape and can be translated to match each other.)

## Intuition
This problem builds upon the standard "Number of Islands" problem. We still need to use **Depth-First Search (DFS)** or **Breadth-First Search (BFS)** to find and traverse each island. The new challenge is identifying if two islands have the exact same shape.

To uniquely identify the shape of an island regardless of its position on the grid, we can record the **path of our traversal**. 
1. As we perform DFS, we append the direction we move to a string (e.g., 'U' for Up, 'D' for Down, 'L' for Left, 'R' for Right).
2. It is crucial to also record when we backtrack (e.g., 'B' for Back), so that different shapes don't accidentally generate the same sequence of forward moves.
3. This generates a unique "shape signature" (a string) for the island.
4. We store these signatures in a **Hash Set**. Because a Hash Set only stores unique elements, duplicate shapes will be ignored.
5. The final answer is simply the size of the Hash Set.

## Complexity
- **Time Complexity:** $O(m \cdot n)$, where $m$ is the number of rows and $n$ is the number of columns. We visit every cell in the grid to find islands, and the DFS visits each land cell exactly once.
- **Space Complexity:** $O(m \cdot n)$. In the worst case (e.g., the entire grid is one big island), the DFS recursion stack can go $m \cdot n$ deep, and our Hash Set will store string signatures that collectively take up to $O(m \cdot n)$ space.