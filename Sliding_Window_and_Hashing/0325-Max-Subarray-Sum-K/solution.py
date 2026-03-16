class Solution:
    # time: O(n) to check the entire nums array of length n
    # space: O(n) to store all sums of subarrays
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # prefix_sum is running total of elements
        prefix_sum = 0
        # max_length is tracker for result
        max_length = 0
        # initially the prefix_sum is 0 at index -1
        sums_at_index = {0:-1}

        for i, num in enumerate(nums):
            # calculate the prefix_sum
            prefix_sum += num

            # store the prefix_sum:i in the hash map
            if prefix_sum not in sums_at_index:
                sums_at_index[prefix_sum] = i

            # calculate the sum needed for valid subarray
            sum_needed = prefix_sum - k

            # check if we have a valid subarray
            if sum_needed in sums_at_index:
                # get the starting index of subarray
                j = sums_at_index[sum_needed]
                # update the max_length tracker
                max_length = max(max_length, i - j)
            # check if we do not have a valid subarray
            
        return max_length