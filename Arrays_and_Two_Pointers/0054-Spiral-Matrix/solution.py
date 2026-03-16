class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # initialize result list to store spiral order values
        result = []
        # handle edge case of empty matrix
        if len(matrix) == 0:
            return result
        # set top boundary to first row
        top = 0
        # set left boundary to first column
        left = 0
        # set bottom boundary to last row
        bottom = len(matrix)-1 
        # set right boundary to last column
        right = len(matrix[0])-1
        # iterate until boundaries cross
        while (top <= bottom and left <= right):
            # go right across the top row
            for i in range(left, right+1):
                result.append(matrix[top][i])
            # move top boundary down
            top += 1
            # go down along the right column
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            # move right boundary left
            right -= 1
            # check if top and bottom boundaries are still valid
            if (top <= bottom):
                # go left across the bottom row
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                # move bottom boundary up
                bottom -= 1
            # check if left and right boundaries are still valid
            if (left <= right):
                # go up along the left column
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                # move left boundary right
                left += 1
        # return the complete spiral order
        return result