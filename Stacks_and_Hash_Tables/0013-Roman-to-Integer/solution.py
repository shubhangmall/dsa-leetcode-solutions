class Solution:
    # time: O(n) for n characters in string s
    # space: O(1) to store the roman numerals (max size 7)
    def romanToInt(self, s: str) -> int:
      # use symbols hash dictionary to convert roman numberals
      symbols = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
      }
      # use result var to track integer
      result = 0
      
      # iterate through the string characters using index
      for i in range(len(s) - 1):
        roman_numeral = s[i] 
        next_roman_numeral = s[i+1] 
        # subtract if next one greater
        if symbols[next_roman_numeral] > symbols[roman_numeral]:
          result -= symbols[roman_numeral]
        # otherwise add if next one smaller or equal
        else:
          result += symbols[roman_numeral]
      
      # convert the last character
      result += symbols[s[-1]]

      return result
        