class Solution:
    # time: O(n * k) — n days in outer loop, k transactions in inner loop
    # space: O(k) — dp table stores k+1 rows of 2 values each
    def maxProfit(self, k: int, prices: List[int]) -> int:
      # dp table with k+1 rows and 2 columns
      # column 0 = max profit NOT holding a stock
      # column 1 = max profit HOLDING a stock
      # -inf for holding because at start we haven't bought anything yet — impossible state
      # 0 for not holding because before any transactions profit is 0
      dp = [[0, -float('inf')] for _ in range(k + 1)]

      # loop through every stock price day by day
      for price in prices:
          # loop through transactions from k down to 1
          # go backwards so each transaction only sees values from the previous day
          # going forward would allow buying and selling on the same day — invalid
          for i in range(k, 0, -1):
            # sell transition — updates not holding state for transaction i
            # best profit not holding = max of:
            # - do nothing — keep previous best not holding profit
            # - sell today — add today's price to holding profit
            dp[i][0] = max(dp[i][0], dp[i][1] + price)

            # buy transition — updates holding state for transaction i
            # best profit holding = max of:
            # - do nothing — keep previous best holding profit
            # - buy today — subtract today's price from previous transaction profit
            # use dp[i-1][0] because buying starts a NEW transaction
            # we build on profit from the PREVIOUS completed transaction
            dp[i][1] = max(dp[i][1], dp[i-1][0] - price)

      # return max profit after at most k transactions
      # dp[k][0] — k transactions done, not holding any stock at the end
      return dp[k][0]


