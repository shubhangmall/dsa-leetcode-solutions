# [427. Construct Quad Tree](https://leetcode.com/problems/construct-quad-tree/)

## Problem Description
Given a `n x n` matrix `grid` of `0's` and `1's` (where `n` is a power of 2), you want to represent the `grid` with a **Quad Tree**.

A Quad Tree is a tree data structure in which each internal node has exactly four children: `topLeft`, `topRight`, `bottomLeft`, and `bottomRight`. 
* If all the values in the current grid are the same (all `1's` or all `0's`), set `isLeaf` to `True` and set `val` to the value of the grid.
* If the values in the current grid are different, set `isLeaf` to `False` and set `val` to any value. Then, divide the current grid into four sub-grids and recursively build the four children.

**Example:**
- **Input:** `grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],...]`
- **Output:** A Quad Tree representation where uniform regions are compressed into leaf nodes.

## Intuition
This problem is a classic application of the **Divide and Conquer** strategy. Since the grid is always a square with a side length that is a power of 2, we can recursively split the grid into four equal quadrants until we reach a state where a quadrant contains only the same value.

**The Strategy:**
1.  **Base Case:** If the current grid section consists of only the same value (all `0`s or all `1`s), create a leaf node with that value.
2.  **Recursive Step:** If the grid section has mixed values:
    * Create a non-leaf node.
    * Divide the current $N \times N$ grid into four $N/2 \times N/2$ sub-grids.
    * Recursively call the function for the `topLeft`, `topRight`, `bottomLeft`, and `bottomRight` quadrants.
3.  **Optimization:** To check if a grid section is uniform, you can either iterate through all cells in that section $O(N^2)$ or use a 2D Prefix Sum (Summed-Area Table) to check the sum of the region in $O(1)$ time after $O(N^2)$ preprocessing.



## Complexity
- **Time Complexity:** $O(N^2 \log N)$ using a simple check for uniformity at each level, or $O(N^2)$ if using a 2D Prefix Sum or by checking if the four children of a node are all leaves with the same value.
- **Space Complexity:** $O(\log N)$ for the recursion stack depth (since the grid size halves each time), plus the space needed to store the resulting Quad Tree nodes.