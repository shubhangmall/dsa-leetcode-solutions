"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    # time: O(n² log n) — check all n² cells at each level, log n levels
    # space: O(log n) — recursive call stack depth
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            # check if all values in this quadrant are the same
            vals_all_same = True
            for i in range(n):
                for j in range(n):
                    # compare each cell to the top left cell of this quadrant
                    if grid[r][c] != grid[r + i][c + j]:
                        # found a different value — not all same
                        vals_all_same = False
                        break
                # break outer loop too if not all same
                if not vals_all_same:
                    break

            # if all values are the same this is a leaf node
            if vals_all_same:
                # return leaf node with the value and isLeaf=True
                return Node(grid[r][c], True, None, None, None, None)

            # if not all same divide into 4 equal quadrants
            half = n // 2

            # recursively build top left quadrant
            top_left = dfs(half, r, c)
            # recursively build top right quadrant
            top_right = dfs(half, r, c + half)
            # recursively build bottom left quadrant
            bottom_left = dfs(half, r + half, c)
            # recursively build bottom right quadrant
            bottom_right = dfs(half, r + half, c + half)

            # return internal node with 4 children and isLeaf=False
            return Node(0, False, top_left, top_right, bottom_left, bottom_right)

        # start DFS with full grid size from top left corner
        return dfs(len(grid), 0, 0)