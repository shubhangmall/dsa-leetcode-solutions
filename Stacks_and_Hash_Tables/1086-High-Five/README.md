# [1086. High Five](https://leetcode.com/problems/high-five/)

## Problem Description
Given a list of scores of different students, return the average score of each student's **top five scores** in the order of each student's ID. Each entry `items[i] = [IDi, scorei]` represents a student's ID and their score.

**Example:**
- Input: `[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]`
- Output: `[[1,87],[2,88]]`

## Intuition
We use a **Hash Map** where keys are student IDs and values are **Min-Heaps**. For each score, we push it into the student's heap. If the heap size exceeds 5, we pop the smallest value. This ensures we only keep the 5 largest scores.



## Complexity
- **Time Complexity:** $O(n \log 5) \approx O(n)$
- **Space Complexity:** $O(S)$ where $S$ is the number of unique students.