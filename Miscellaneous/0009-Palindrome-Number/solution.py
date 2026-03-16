class Solution:
    # time: O(n) to convert and reverse n digits
    # space: O(n) to store n digits
    def isPalindrome(self, x: int) -> bool:
        # check if x is negative then return false
        if x < 0:
          return False
        # convert x to string
        x = str(x)
        # reverse the string
        reversed_x = x[::-1]

        return x == reversed_x

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers are never palindromes
        if x < 0:
            return False
        
        # store original to compare at end
        original = x
        reversed_num = 0
        
        # build reversed number digit by digit
        while x > 0:
            # get last digit
            last_digit = x % 10
            # add last digit to reversed number
            reversed_num = reversed_num * 10 + last_digit
            # remove last digit from x
            x = x // 10
        
        # if original equals reversed it is a palindrome
        return original == reversed_num
        