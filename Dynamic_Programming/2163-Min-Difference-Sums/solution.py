import heapq

class Solution:
    # time: O(n log n) — heap operations across 2n elements
    # space: O(n) — two heaps and two arrays each storing at most n elements
    def minimumDifference(self, nums: List[int]) -> int:
      # len(nums) = 3 * n
      total_length = len(nums)
      n = total_length // 3
    
      prefix_sums_min = [0] * (total_length + 1) # we need extra place for first prefix sum
      current_sum = 0 
      max_heap = [] # max heap to track the n smallest elements with largest at the top

      for i, num in enumerate(nums[:2*n], 1): # start tracking prefix sum from index 1 to 2n
        current_sum += num
        heapq.heappush(max_heap, -num) # push onto the max heap negative value

        if len(max_heap) > n: # check if the max heap has more than n elements
          # get sum of n smallest elements by subtracting largest from running sum
          largest = -heapq.heappop(max_heap)
          current_sum -= largest

        prefix_sums_min[i] = current_sum # store min sum of n elements from first i elements

      suffix_max_sums = [0] * (total_length + 1) # we need extra place for first suffix sum
      current_sum = 0
      min_heap = []

      # loop through right part last n elements
      for i in range(total_length, n, -1):
        num = nums[i - 1] # because nums is 0 index the last element we subtract 1
        current_sum += num
        heapq.heappush(min_heap, num) # push onto the min heap value

        if len(min_heap) > n: # check if the min heap has more than n elements
          # get sum of n smallest elements by subtracting smallest from running sum
          smallest = heapq.heappop(min_heap)
          current_sum -= smallest

        suffix_max_sums[i] = current_sum

      # find the minimum difference
      min_diff = float('inf')
      for split_point in range(n, 2*n + 1):
        difference = prefix_sums_min[split_point] - suffix_max_sums[split_point + 1]
        min_diff = min(min_diff, difference)

      return min_diff



        