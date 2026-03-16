class Solution:
    # time: O(n²) — two nested loops through nums
    # space: O(n) — DP array stores one value per element
    def lengthOfLIS(self, nums: List[int]) -> int:
        # every element is at minimum a subsequence of length 1 by itself
        LIS = [1] * len(nums)

        # scan right to left so each position knows the best result ahead of it
        for i in range(len(nums) - 1, -1, -1):
            # check every element to the right of i
            for j in range(i + 1, len(nums)):
                # if nums[i] is smaller than nums[j] then i can extend into j
                if nums[i] < nums[j]:
                    # update LIS[i] to be the longest subsequence starting at i
                    # 1 is for including i itself, LIS[j] is the best from j onwards
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # the answer is the longest subsequence found across all starting positions
        return max(LIS)