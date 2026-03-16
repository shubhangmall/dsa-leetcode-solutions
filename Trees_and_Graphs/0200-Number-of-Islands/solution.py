class Solution:
    # time: O(m x n) - every cell visited at most once
    # space: O(m x n) - DFS call stack depth if entire grid is one island
    def numIslands(self, grid: List[List[str]]) -> int:
      # m is rows - greater than or equal to 1
      # n is cols - less than or equal to 300
      # each grid element is '0' or '1' str

      # track result
      islands = 0

      # get rows, cols
      m = len(grid)
      n = len(grid[0])

      def dfs(row,col):
        # stop searching if out of bounds
        if row < 0 or row >= m or col < 0 or col >= n:
          return

        # stop searching if water found or already searched
        if grid[row][col] == "0":
          return

        # now it must be a 1 or function returns
        # so mark it as searched by setting it to 0
        grid[row][col] = "0"
        # recursively explore each path
        # search down
        dfs(row + 1, col)
        # search up
        dfs(row - 1, col)
        # search right
        dfs(row, col + 1)
        # search left
        dfs(row, col - 1)

      for row in range(m):
        for col in range(n):
          # after dfs searched or water elements are 0
          # so check if the element is a 1
          if grid[row][col] == "1": # unvisited island
            islands += 1 # found a new island
            dfs(row, col) # find more adjacent islands
      
      return islands

        