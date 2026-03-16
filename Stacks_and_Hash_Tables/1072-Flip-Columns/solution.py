class Solution:
    # time: no rows have equal values O(m x n) 
    # check each row and flip each column
    # space: hash only fills rows which can be O(m)
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
      # use hash map that sets missing keys to 0
      count = defaultdict(int)

      # loop through each row
      for row in matrix:
        # convert row array to hash key tuple
        row_as_key = tuple(row)

        # check if the first element is 1
        if row[0]:
          # flip the row elements
          flipped_row = []
          for row_element in row:
            # flip 1s to 0s
            if row_element == 1:
              flipped_row.append(0)
            # flip 0s to 1s
            else:
              flipped_row.append(1)
          # convert the flipped row to hash key tuple
          row_as_key = tuple(flipped_row)
        
        # we either have identical row or flipped identical row
        # able to add to the hash map row_as_key:count
        count[row_as_key] += 1

      # return the maximium identical row value from count hash map
      return max(count.values())
