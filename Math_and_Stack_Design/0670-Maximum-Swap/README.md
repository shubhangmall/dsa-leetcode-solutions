# [670. Maximum Swap](https://leetcode.com/problems/maximum-swap/)

## Problem Description
You are given a non-negative integer `num`. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

**Example:**
- **Input:** `num = 2736`
- **Output:** `7236` (Swap 2 and 7)
- **Input:** `num = 9973`
- **Output:** `9973` (No swap needed)

## Intuition
To maximize the number with a single swap, we want to find the **leftmost** digit that can be replaced by a **larger** digit that appears somewhere to its right. If there are multiple candidates for the "larger digit" on the right, we should pick the largest one (and specifically the one furthest to the right among those) to gain the most value.

**The Strategy:**
1.  Convert the number into a list of characters to allow for easy swapping and indexing.
2.  Traverse the digits from **right to left** while maintaining a record of the maximum digit seen so far (`max_digit`) and its index (`max_i`).
3.  As we scan backwards:
    * If the current digit is greater than our `max_digit`, we update our maximum and its position.
    * If the current digit is **smaller** than our `max_digit`, this digit is a candidate for a swap. We store this current index as `swap_i` and the stored max index as `swap_j`.
4.  Because we continue scanning all the way to the left, `swap_i` will eventually represent the **leftmost** possible digit that has a larger value to its right.
5.  Perform the swap and convert the list back into an integer.

## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the number of digits in the input. We iterate through the digits once from right to left.
- **Space Complexity:** $O(n)$ to store the string/list representation of the number.