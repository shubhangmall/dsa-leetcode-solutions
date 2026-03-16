# [140. Word Break II](https://leetcode.com/problems/word-break-ii/)

## Problem Description
Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in **any order**.

The same word in the dictionary may be reused multiple times in the segmentation.

**Example:**
- **Input:** `s = "catsanddog"`, `wordDict = ["cat","cats","and","sand","dog"]`
- **Output:** `["cats and dog","cat sand dog"]`

## Intuition
This problem requires exploring all possible ways to partition a string into valid words, which makes **Backtracking** the most natural approach. By treating the string as a sequence of characters, we can try to "cut" the string at various points to see if the resulting prefix exists in our dictionary.

**The Strategy:**
1.  **Efficient Lookup:** Convert the `wordDict` into a **Hash Set** to ensure that checking if a substring is a valid word takes $O(1)$ time.
2.  **State Exploration:** Use a recursive `backtrack` function that tracks the current index `i` in the string `s`.
3.  **Path Building:** * Maintain a list `curr_words` to act as a stack, storing the valid words found in the current branch of exploration.
    * For a given starting position `i`, iterate through all possible ending positions `j` to form a substring.
    * If `s[i:j+1]` is in the dictionary, push it to `curr_words` and recurse starting from `j + 1`.
4.  **Backtracking:** After the recursive call returns (meaning we've explored all possibilities following that specific word), **pop** the word from `curr_words` to reset the state for the next iteration of the loop.
5.  **Base Case:** When the starting index `i` reaches the end of the string, it means the current path of words successfully covers the entire string. We join the words with spaces and add the resulting sentence to our `result` list.



## Complexity
- **Time Complexity:** $O(2^n)$, where $n$ is the length of the string `s`. In the worst case (e.g., every character and every combination of characters is a valid word), there are $2^{n-1}$ possible ways to partition the string.
- **Space Complexity:** $O(n)$, which accounts for the maximum depth of the recursion stack and the `curr_words` list, both of which are bounded by the length of the input string.