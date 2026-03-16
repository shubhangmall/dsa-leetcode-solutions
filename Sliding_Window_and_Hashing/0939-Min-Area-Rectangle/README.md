# [939. Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/)

## Problem Description
You are given an array of points in the $X-Y$ plane `points` where `points[i] = [xi, yi]`.

Return the **minimum area** of a rectangle formed from these points, with sides parallel to the $X$ and $Y$ axes. If there is not any such rectangle, return `0`.

**Example:**
- **Input:** `points = [[1,1],[1,3],[3,1],[3,3],[2,2]]`
- **Output:** `4` (The rectangle formed by (1,1), (1,3), (3,1), and (3,3))

## Intuition
A rectangle with sides parallel to the axes is uniquely defined by two diagonal points: $(x_1, y_1)$ and $(x_2, y_2)$. 
If we pick any two points from the input and treat them as the **bottom-left** and **top-right** corners of a potential rectangle:
1. They must not share the same $x$ or $y$ coordinate (otherwise, they form a line, not a diagonal).
2. The other two corners needed to complete the rectangle must also exist in our set of points. These coordinates would be $(x_1, y_2)$ and $(x_2, y_1)$.



**The Strategy:**
- Store all points in a **Hash Set** for $O(1)$ lookup.
- Use a nested loop to pick every pair of points $(x_1, y_1)$ and $(x_2, y_2)$.
- Check if $(x_1, y_2)$ and $(x_2, y_1)$ are present in the set.
- If they are, calculate the area $|x_1 - x_2| \cdot |y_1 - y_2|$ and track the minimum.

## Complexity
- **Time Complexity:** $O(n^2)$, where $n$ is the number of points. We iterate through all pairs of points.
- **Space Complexity:** $O(n)$, as we store all $n$ points in a Hash Set to allow for fast coordinate lookups.