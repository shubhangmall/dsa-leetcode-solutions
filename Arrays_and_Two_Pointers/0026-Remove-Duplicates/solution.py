class Solution:
  # time: O(n) if no dupliactes for n elements in nums
  # space: O(1) since in-place algorithm
    def removeDuplicates(self, nums: List[int]) -> int:
      # use slow tracking pointer at second integer
      left = 1

      # use fast checking pointer to iterate through nums array
      for right in range(1, len(nums)):
        # check if the integers are different
        if nums[right] != nums[left - 1]:
          # replace the tracked value with new checked value
          nums[left] = nums[right]
          # track the next integer
          left += 1
      
      # return how many unique integers were tracked
      return left
        