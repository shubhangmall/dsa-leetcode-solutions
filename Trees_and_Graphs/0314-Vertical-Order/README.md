# [314. Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/)

## Problem Description
Given the `root` of a binary tree, return the **vertical order traversal** of its nodes' values (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from **left to right**.

**Example:**
- **Input:** `root = [3,9,20,null,null,15,7]`
- **Output:** `[[9],[3,15],[20],[7]]`
- **Explanation:**
  - Column -1: [9]
  - Column  0: [3, 15]
  - Column  1: [20]
  - Column  2: [7]

## Intuition
To traverse the tree vertically, we need to assign a "column index" to each node. We can define the root as column `0`. Then:
* A left child has a column index of `column - 1`.
* A right child has a column index of `column + 1`.

Since the problem requires a **top-to-bottom** order for nodes in the same column, a **Breadth-First Search (BFS)** is ideal. BFS naturally visits nodes level by level.

**The Strategy:**
1.  Use a **Queue** for BFS, storing pairs of `(node, column_index)`.
2.  Use a **Hash Map** (or Dictionary) where keys are column indices and values are lists of node values.
3.  Track the `min_column` and `max_column` seen so far to avoid sorting the Hash Map keys at the end.
4.  As you traverse, append each node's value to its corresponding column list in the map.
5.  Finally, iterate from `min_column` to `max_column` and collect the lists into a result array.

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the number of nodes in the tree. We visit each node exactly once using BFS.
- **Space Complexity:** $O(n)$ to store the Hash Map and the Queue for BFS.