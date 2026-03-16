# [155. Min Stack](https://leetcode.com/problems/min-stack/)

## Problem Description
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
* `MinStack()` initializes the stack object.
* `void push(int val)` pushes the element `val` onto the stack.
* `void pop()` removes the element on the top of the stack.
* `int top()` gets the top element of the stack.
* `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with $O(1)$ time complexity for each function.

## Intuition
To achieve $O(1)$ for all operations, we use a **Two-Stack approach**:
1.  **Main Stack:** Stores all the elements pushed into the data structure.
2.  **Min Stack:** Stores the "running minimum." 

When we push a value onto the Main Stack, we compare it with the current top of the Min Stack. If the new value is less than or equal to the current minimum, we push it onto the Min Stack as well. When we pop from the Main Stack, if the value being removed is the current minimum (i.e., it matches the top of the Min Stack), we pop it from the Min Stack too. 

This ensures that the top of the Min Stack always represents the minimum value currently present in the Main Stack.



## Complexity
- **Time Complexity:** $O(1)$ for all operations (`push`, `pop`, `top`, `getMin`), as stack operations are constant time.
- **Space Complexity:** $O(n)$, where $n$ is the number of elements pushed, as we potentially store each element in both stacks.