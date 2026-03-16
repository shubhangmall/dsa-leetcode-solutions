class Solution:
    # time-complexity: 
    # - accessing all numbers O(n)
    # - accessing/inserting hash O(1)
    # -- overall: O(n)

    # space-complexity:
    # - using hash may take all numbers 
    # -- overall: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # use empty hash dictionary for seen numbers
      seen = {}

      # go through the indices and numbers in the array
      for i, num in enumerate(nums):
        # calculate the complement using the target and current number
        complement = target - num

        # check if the complement already exists in the seen hash dictionary
        if complement in seen:
          # if it does then return the complement and current numbers indices
          return [seen[complement], i]
        # if the complement does not exist then add it to the hash dictionary
        # set the value as the index, the key is the current number
        else:
          seen[num] = i