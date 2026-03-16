# [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)

## Problem Description
We have `n` jobs, where every job is represented by three integers: `startTime[i]`, `endTime[i]`, and `profit[i]`.

Return the maximum profit you can take such that there are no two jobs in the subset with overlapping time ranges. If you choose a job that ends at time `X`, you can start another job that starts at time `X`.

**Example:**
- **Input:** `startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]`
- **Output:** `120`
- **Explanation:** The subset chosen is the first and fourth job (Profit = 50 + 70 = 120).

## Intuition
This problem is a variation of the "Weighted Interval Scheduling" problem. Since each decision (to take or skip a job) affects future availability, we use **Depth First Search (DFS) with Memoization** to explore the optimal path.

**The Strategy:**
1.  **Sorting:** We sort the jobs by their **start times**. This allows us to use binary search to quickly find the next available job that starts after the current one ends.
2.  **Decision Making (The "Take or Skip" Pattern):**
    * **Skip:** We move to the next immediate job (`i + 1`).
    * **Take:** We add the current job's profit and jump to the next **compatible** job.
3.  **Binary Search:** To avoid checking every single job to find the next compatible one, we use `bisect_left` (or `bisect`) on the sorted `intervals`. This finds the first job `j` where `intervals[j].startTime >= current_job.endTime`.
4.  **Memoization:** We use a `cache` to store the maximum profit possible starting from index `i`. This transforms an exponential time complexity into a linear number of states.



## Complexity
- **Time Complexity:** $O(n \log n)$. Sorting the jobs takes $O(n \log n)$. The DFS explores $n$ states, and inside each state, we perform a binary search which takes $O(\log n)$.
- **Space Complexity:** $O(n)$ to store the `intervals` list, the recursion stack, and the `cache` dictionary.