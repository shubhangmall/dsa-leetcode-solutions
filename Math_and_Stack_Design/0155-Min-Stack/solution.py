class MinStack:
    # time: O(1) for all functions
    # space: O(n) for stack space
    def __init__(self):
      self.main_stack = []
      self.min_stack = []
        

    def push(self, val: int) -> None:
      # always push val element onto main stack
      self.main_stack.append(val)

      # only push val element onto min stack if it is smaller
      if self.min_stack:
        last_min_val = self.min_stack[-1]
        # check if val to push is smaller or equal
        if val <= last_min_val:
          # push the val onto the min stack
          self.min_stack.append(val)

      else:
        self.min_stack.append(val)

        

    def pop(self) -> None:
      # only from min stack if popped element is minimum element
      if self.main_stack[-1] == self.min_stack[-1]:
        self.min_stack.pop()

      # always pop val element from main stack
      self.main_stack.pop()
        

    def top(self) -> int:
      return self.main_stack[-1]
        

    def getMin(self) -> int:
      return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()