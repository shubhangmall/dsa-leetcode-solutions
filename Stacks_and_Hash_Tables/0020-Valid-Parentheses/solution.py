class Solution:
    # time: O(n) to check the entire string
    # space: O(n) to create entire stack for invalid string
    def isValid(self, s: str) -> bool:
      # constant variable to check for opening brackets
      opening_brackets = "({["
      # hash dictionary to check for matching brackets
      matches = {
        ')':'(',
        '}':'{',
        ']':'['
      }
      # stack to check if string has valid closing brackets
      stack = []

      # check each character in the string
      for char in s:
        # check if the character is an opening bracket
        if char in opening_brackets:
          # add the opening bracket to the stack
          stack.append(char)
        else:
          # check if the character is a closing bracket
          if char in matches:
            # check if the stack has its matching closing bracket
            if stack and stack[-1] == matches[char]:
              # they match so move on to the next character
              # pop its opening bracket from the stack
              stack.pop()
            else:
              # return false because there was no match
              return False

      # if the stack is empty then the string is valid
      return len(stack) == 0
