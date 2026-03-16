# [1760. Minimum Limit of Balls in a Bag](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/)

## Problem Description
You are given an integer array `nums` where the $i^{th}$ bag contains `nums[i]` balls. You are also given an integer `maxOperations`.

You can perform the following operation at most `maxOperations` times:
* Take any bag of balls and divide it into two new bags with a positive number of balls.
* For example, a bag of `5` balls can become two bags of sizes `1` and `4`, or `2` and `3`.

Your penalty is the **maximum** number of balls in a bag. You want to **minimize** this penalty.

**Example:**
- **Input:** `nums = [9], maxOperations = 2`
- **Output:** `3`
- **Explanation:** - Divide [9] into [3, 6] (1 operation).
  - Divide [6] into [3, 3] (1 operation).
  - Bags are [3, 3, 3]. Max is 3.

## Intuition
This is a "Minimize the Maximum" problem, which is a classic signal for **Binary Search on Answer**. Instead of trying to figure out how to split the bags, we pick a potential penalty `mid` and check if it is possible to achieve it within `maxOperations`.

**The Strategy:**
1.  **Search Range:** The minimum possible penalty is `1` and the maximum is `max(nums)`.
2.  **Feasibility Check (isPossible):** For a target penalty `mid`, how many operations are needed for a bag with `n` balls?
    * To make every bag have at most `mid` balls, a bag of size `n` needs to be split into $\lceil n / mid \rceil$ pieces.
    * The number of operations required is `(n - 1) // mid`. 
    * Sum these operations for all bags. If the total is $\le$ `maxOperations`, then `mid` is a valid penalty.
3.  **Binary Search:** * If `mid` is possible, try a smaller penalty (`high = mid`).
    * If `mid` is not possible, we must allow a larger penalty (`low = mid + 1`).



## Complexity
- **Time Complexity:** $O(n \log M)$, where $n$ is the number of bags and $M$ is the maximum value in `nums`. We perform binary search over the range $[1, M]$, and for each step, we iterate through all $n$ bags.
- **Space Complexity:** $O(1)$ as we only use a few variables for the binary search boundaries and the operation counter.