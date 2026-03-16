# [1762. Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view/)

## Problem Description
There are `n` buildings in a line. You are given an integer array `heights` of size `n` where `heights[i]` represents the height of the `i-th` building.

To the right of the buildings is the ocean. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a **smaller** height.

Return a list of indices of buildings that have an ocean view, sorted in increasing order.

**Example:**
- **Input:** `heights = [4,2,3,1]`
- **Output:** `[0,2,3]`
- **Explanation:** - Building 0 (height 4) has a view (all to the right are 2, 3, 1).
  - Building 1 (height 2) does not (building 2 is taller).
  - Building 2 (height 3) has a view (only 1 is to the right).
  - Building 3 (height 1) has a view (no buildings to the right).

## Intuition
The key to this problem is realizing that a building has a view only if it is taller than the **tallest** building to its right. Instead of checking every building against every other building to its right ($O(n^2)$), we can traverse the array from **right to left**:

1. Keep track of the `max_height` seen so far (starting at 0).
2. Iterate from the last building to the first.
3. If the current building is taller than `max_height`, it has a view.
4. Update `max_height` and add the current index to our result.
5. Since we collect indices from right to left, we simply reverse the list at the end.



## Complexity
- **Time Complexity:** $O(n)$, where $n$ is the number of buildings, as we iterate through the array once.
- **Space Complexity:** $O(1)$ (excluding the space for the output list), as we only store a single variable for the maximum height.