# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time: O(n) to traverse all nodes
    # space: O(n) to store all nodes in the hashmap
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # handle edge case of empty tree
        if not root:
            return []

        # queue stores (node, column) pairs for BFS
        # root starts at column 0
        queue = deque()
        queue.append((root, 0))

        # hashmap stores column -> list of node values
        cols = defaultdict(list)

        # track the leftmost and rightmost column seen
        min_col = 0
        max_col = 0

        # BFS loop — keep going until queue is empty
        while queue:
            # get the next node and its column from the front of queue
            node, col = queue.popleft()

            # update leftmost column if current col is smaller
            min_col = min(min_col, col)
            # update rightmost column if current col is larger
            max_col = max(max_col, col)

            # add current node value to its column list
            cols[col].append(node.val)

            # if left child exists add it to queue one column to the left
            if node.left:
                queue.append((node.left, col - 1))

            # if right child exists add it to queue one column to the right
            if node.right:
                queue.append((node.right, col + 1))

        # build result list by going from leftmost to rightmost column
        result = []
        for c in range(min_col, max_col + 1):
            # append each column's list of values to result
            result.append(cols[c])

        # return the final vertical order result
        return result
        