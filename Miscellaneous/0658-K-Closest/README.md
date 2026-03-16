# [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

## Problem Description
Given a **sorted** integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:
* `|a - x| < |b - x|`, or
* `|a - x| == |b - x|` and `a < b`

**Example:**
- **Input:** `arr = [1,2,3,4,5], k = 4, x = 3`
- **Output:** `[1,2,3,4]`

## Intuition
Since the array is already sorted, the $k$ closest elements will always form a **contiguous subarray**. The problem essentially asks us to find the starting index `left` of this subarray of length `k`.

While we could find the position of `x` and expand outwards, a more efficient way is to use **Binary Search** to find the optimal left boundary.

**The Strategy (Binary Search on the Left Bound):**
1.  **Search Space:** The possible starting index `left` ranges from `0` to `len(arr) - k`.
2.  **Comparison Logic:** For a mid-point `mid`, we are comparing two potential windows:
    * One starting at `mid` (includes `arr[mid]`).
    * One starting at `mid + 1` (includes `arr[mid + k]`).
3.  **Decision Rule:**
    * If `x - arr[mid] > arr[mid + k] - x`, it means `arr[mid]` is farther from `x` than `arr[mid + k]`. Therefore, the window should shift right (`low = mid + 1`).
    * Otherwise, `mid` is a better or equal starting point than `mid + 1`, so we move left (`high = mid`).
4.  **Result:** Once the binary search concludes, the window starts at `low` and ends at `low + k`.



## Complexity
- **Time Complexity:** $O(\log(n - k) + k)$. The binary search takes $O(\log(n - k))$ to find the starting index, and slicing the array to return the result takes $O(k)$.
- **Space Complexity:** $O(k)$ or $O(1)$ depending on whether you count the output list. The search itself uses constant extra space.