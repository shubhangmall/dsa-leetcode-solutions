# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## Problem Description
Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

An integer is a palindrome when it reads the same forward and backward. For example, `121` is a palindrome while `123` is not.

**Example:**
- **Input:** `x = 121`
- **Output:** `true`
- **Input:** `x = -121`
- **Output:** `false` (Reads as `121-` from right to left)

## Intuition
The most straightforward way is to convert the number to a string and check if it's the same reversed. However, the challenge often implies solving it **without** extra string space.

**The Strategy (Reversing Half the Number):**
1.  **Negative Numbers:** All negative numbers are not palindromes (the `-` sign makes them asymmetrical).
2.  **Trailing Zeros:** If a number ends in `0`, it must be `0` itself to be a palindrome (otherwise, it would need to start with `0`).
3.  **Reversal:** We can reverse the second half of the number and compare it with the first half. 
    * To get the last digit: `x % 10`
    * To move to the next digit: `x // 10`
    * To build the reversed number: `reversed_num = (reversed_num * 10) + last_digit`
4.  **Stopping Point:** We know we've reached the middle when the original number becomes less than or equal to the reversed number.
5.  **Comparison:** * If the length is even, `x == reversed_num`.
    * If the length is odd, the middle digit doesn't matter, so we check `x == reversed_num // 10`.



## Complexity
- **Time Complexity:** $O(\log_{10}(n))$. We divide the input by 10 in every iteration, so the number of iterations is the number of digits in the input.
- **Space Complexity:** $O(1)$ as we only store a few integer variables regardless of the size of the input.