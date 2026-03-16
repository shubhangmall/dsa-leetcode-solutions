# [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

## Problem Description
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day, and an integer `k`. Find the maximum profit you can achieve with at most `k` transactions. You must sell the stock before you buy again.

**Example:**
- **Input:** `k = 2, prices = [3,2,6,5,0,3]`
- **Output:** `7`
- **Explanation:** Buy on day 2 (price 2), sell on day 3 (price 6). Buy on day 5 (price 0), sell on day 6 (price 3). Total = $4 + 3 = 7$.

## Intuition
Your approach uses **Bottom-Up Dynamic Programming** with a space-optimized table. The core idea is to track the "net worth" of your account across $k$ different potential transactions for every single day.

**The Strategy:**
1.  **State Representation:** You use a DP table `dp[i][state]`, where `i` is the number of transactions allowed (from 1 to $k$) and `state` is either **Not Holding (0)** or **Holding (1)**.
2.  **The "Reverse" Inner Loop:** By iterating $k$ down to 1, you ensure that the updates for transaction $i$ are based on the results of transaction $i-1$ from the *previous* day. This prevents "teleporting" through multiple transactions on a single day.
3.  **Transitions:**
    * **Sell Transition (`dp[i][0]`):** You decide whether to keep your current profit or sell the stock you were holding (`dp[i][1] + price`).
    * **Buy Transition (`dp[i][1]`):** You decide whether to keep holding what you have or start transaction $i$ by buying a stock using the profit from the *previous* completed transaction (`dp[i-1][0] - price`).
4.  **Initialization:** Initializing the "Holding" state to $-\infty$ is crucial because you cannot be in a "holding" state without having spent money first.



## Complexity
- **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of days and $k$ is the maximum number of transactions. Every price is processed against every transaction level exactly once.
- **Space Complexity:** $O(k)$ to store the DP table. While the logic conceptually covers $n$ days, only the most recent results for each transaction $k$ are needed, allowing for the $O(k)$ space optimization.