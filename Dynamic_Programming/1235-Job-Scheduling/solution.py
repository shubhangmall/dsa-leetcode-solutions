class Solution:
    # time: O(n log n) — sorting + binary search for each of n jobs
    # space: O(n) — cache stores result for each job
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
        # combine three input arrays into tuples and sort by start time
        intervals = sorted(zip(startTime, endTime, profit))
        # intervals = [(1,3,50), (2,4,10), (3,5,40), (3,6,70)]
        
        # store results of dfs so we don't recalculate
        cache = {}

        def dfs(i):
          # base case as all jobs processed
          if i == len(intervals):
            return 0
          # if already checked return the max profit
          if i in cache:
            return cache[i]

          # choice 1: skip interval i by recursive check next interval i+1
          max_profit = dfs(i + 1) 

          # choice 2: take interval i
          endTime = intervals[i][1]
          # find first interval starting at or after current interval's end time
          j = bisect.bisect(intervals, (endTime, -1, -1)) # binary search
          # best profit from next compatible interval using j
          profit = intervals[i][2]
          best_profit = profit + dfs(j)
          # store in cache and result the maximum of already calculated or next job
          cache[i] = max_profit = max(max_profit, best_profit)
          
          return max_profit

        return dfs(0)