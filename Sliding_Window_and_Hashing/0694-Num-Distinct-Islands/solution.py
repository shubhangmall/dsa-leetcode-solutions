class Solution:
    # time: O(m x n) to search for each grid element 
    # space: O(m x n) to DFS call each element
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # m is rows - greater than or equal to 1
        # n - cols - less than or equal to 300
        # each grid element is '0' or '1'

        # track result using hash set for unique search path lists
        islands = set()

        # get the total number of rows from grid
        m = len(grid)
        # get the total number of cols from grid
        n = len(grid[0])

        # dfs search logic
        def dfs(row: int, col: int, direction: str):
            # stop searching if out of bounds or from a water element 0
            out_of_bounds = row < 0 or row >= m or col < 0 or col >= n
            if out_of_bounds or grid[row][col] == 0:
                return

            # now it must be island element 1
            # mark it searched by setting it to 0
            grid[row][col] = 0
            # also mark it searched by adding direction to search path
            search_path.append(direction)

            # recursively search all directions
            # search down
            dfs(row+1, col, "D")
            # search up
            dfs(row-1, col, "U")
            # search left
            dfs(row, col-1, "L")
            # search right
            dfs(row, col+1, "R")

            # if none of those found anything we use B to go back 
            # everything is searched so no grid element changes
            search_path.append("B")

        # iterate through entire grid
        for row in range(m):
            for col in range(n):
                # only start searching from an island elemnt 1
                if grid[row][col] == 1:
                    # search current island and get its shape
                    # search direction list
                    search_path = []
                    # implement the dfs search logic
                    dfs(row, col, "S") # use string S to start path
                    # hash set only accepts unique search paths
                    islands.add(tuple(search_path))

        # return the length of hash set for number of unique islands
        return len(islands)
        