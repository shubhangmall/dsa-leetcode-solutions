class Solution:
    # time: O(m * n * 4^L) — every cell is a starting point, DFS branches 4 directions L times
    # space: O(L) for the path set and recursive call stack both at most L deep  
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(row, col, word_idx):
          if word_idx == len(word):
            return True
          if (row < 0 or col < 0) or (row >= rows or col >= cols) or (word[word_idx] != board[row][col]) or (row, col) in path:
            return False

          path.add((row, col))

          result =  dfs(row + 1, col, word_idx + 1) or dfs(row - 1, col, word_idx + 1) or dfs(row, col + 1, word_idx + 1) or dfs(row, col - 1, word_idx + 1)
          
          path.remove((row, col))
          return result

        for row in range(rows):
          for col in range(cols):
            if dfs(row, col, 0): return True

        return False