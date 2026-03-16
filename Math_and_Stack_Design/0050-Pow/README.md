# [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

## Problem Description
Implement `pow(x, n)`, which calculates $x$ raised to the power $n$ (i.e., $x^n$).

**Example:**
- **Input:** `x = 2.00000, n = 10`
- **Output:** `1024.00000`
- **Input:** `x = 2.00000, n = -2`
- **Output:** `0.25000` (Since $2^{-2} = \frac{1}{2^2} = \frac{1}{4} = 0.25$)

## Intuition
The naive approach of multiplying $x$ by itself $n$ times would take $O(n)$ time, which is too slow for large values of $n$. Instead, we use the **Binary Exponentiation** (also known as **Exponentiation by Squaring**) technique.

The core idea is to split the power in half at each step:
- If $n$ is even: $x^n = (x^2)^{n/2}$
- If $n$ is odd: $x^n = x \cdot (x^2)^{(n-1)/2}$

For negative exponents, we can calculate $pow(x, -n)$ as $\frac{1}{pow(x, n)}$. This approach reduces the number of multiplications significantly by doubling the base and halving the exponent in each step.



## Complexity
- **Time Complexity:** $O(\log n)$, as the exponent $n$ is divided by 2 in every iteration or recursive call.
- **Space Complexity:** $O(\log n)$ for the recursive approach (due to the call stack) or $O(1)$ for the iterative approach.