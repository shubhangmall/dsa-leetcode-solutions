class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # track frequency of each number in current window
        count = defaultdict(int)
        # count of valid subarrays with exactly k distinct integers
        result = 0

        # leftmost valid left boundary — window has exactly k distinct
        l_far = 0
        # rightmost valid left boundary — window has exactly k distinct
        l_near = 0

        # expand right pointer through every element
        for r in range(len(nums)):
            # add right element to window and increment its frequency
            count[nums[r]] += 1

            # if window has more than k distinct integers shrink from left
            while len(count) > k:
                # decrement frequency of leftmost element
                count[nums[l_near]] -= 1
                # if frequency hits 0 remove it from window entirely
                if count[nums[l_near]] == 0:
                    count.pop(nums[l_near])
                # move left pointer forward
                l_near += 1
                # reset l_far to match l_near since window changed
                l_far = l_near

            # find rightmost valid left by shrinking while leftmost element has duplicates
            while count[nums[l_near]] > 1:
                # decrement frequency of leftmost element
                count[nums[l_near]] -= 1
                # move l_near forward to find rightmost valid left boundary
                l_near += 1

            # if window has exactly k distinct count all valid subarrays ending at r
            if len(count) == k:
                # every position between l_far and l_near is a valid left boundary
                result += l_near - l_far + 1

        # return total count of good subarrays
        return result