class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # time: O(m² x n²) — outer loop runs O(m x n) times, each iteration scans O(m x n)
        # space: O(1) — board modified in place
        crushed = True
        
        while crushed:
            rows = m = len(board)
            cols = n = len(board[0])

            # mark step

            # reset to stop loop if nothing crushed
            crushed = False
            
            # check horizontally for groups of three or more candies
            for r in range(rows):
                for c in range(cols - 2):
                    # check if three or more candies are same type
                    if (abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2])) and board[r][c] != 0:
                        # mark candies to be crushed as negative values
                        crushed = True
                        board[r][c] = -abs(board[r][c])
                        board[r][c+1] = -abs(board[r][c+1])
                        board[r][c+2] = -abs(board[r][c+2])

            # check vertical groups of three or more candies
            for r in range(rows - 2):
                for c in range(cols): 
                    # check if three or more candies are same type
                    if (abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c])) and board[r][c] != 0:
                        # mark candies to be crushed as negative values
                        crushed = True
                        board[r][c] = -abs(board[r][c])
                        board[r+1][c] = -abs(board[r+1][c])
                        board[r+2][c] = -abs(board[r+2][c])

            # drop step

            # loop through each column
            for c in range(cols):
                slow = rows - 1

                for fast in range(rows - 1, -1, -1):
                    # check for non-marked values
                    if board[fast][c] > 0:
                        # place the non-marked values at the bottom of the col
                        board[slow][c] = board[fast][c]
                        # move slow pointer up to row -1
                        slow -= 1

                # any remaining cells replace with 0 above
                while slow >= 0:
                    board[slow][c] = 0
                    slow -= 1

        # return the board after crushing 
        return board 

            