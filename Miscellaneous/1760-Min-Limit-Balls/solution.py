class Solution:
  # time: O(n log(max(nums))) — binary search over answer range, O(n) check each step
  # space: O(1) — only using a few variables
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
      # penalty = maximum number of balls in a bag
      # minimum possible penalty = 1 as every bag has 1 ball at least
      # maximum possible penalty = max(nums) no splitting get the bag with the largest number of balls
      left, right = 1, max(nums)

      # binary search loop
      while left < right: # looking for the minimum valid value so when left and right meet we get result
        mid = (left + right) // 2
        
        # check if mid works
        # for each bag in nums calculate how many splits it needs if the limit is mid
        # bag = 9, mid = 3
        # ceil(9/3) - 1 = 2 splits needed
        # ceil(n/mid) - 1 = number of splits needed
        operations = 0
        for n in nums:
          operations += math.ceil(n / mid) - 1

        if operations <= maxOperations:
          # mid is possible, try smaller bag sizes
          right = mid
        else:
          # mid fails, try bigger bag sizes
          left = mid + 1

      # when loop finishes left == right which is minimum valid penalty
      return left

        