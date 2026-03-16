class Solution:
    # time: 
    # - O(n) for n characters in s
    # - O(m) for m characters in t
    # overall: O(n+m)
    # space:
    # - O(n) for all n unique characters from s
    # overall: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
      # use counts hash dict for source of truth
      counts = {}

      # go through each character in string s
      for char in s:
        # check if it is not in the counts hash
        if char not in counts:
          # add value of 1 for key of char to count it
          counts[char] = 1
        # check if it is in the counts hash
        else:
          # increment value by 1 for key of char to count it
          counts[char] += 1

      # go through each character in string t
      for char in t:
        # check if it is not in the counts hash
        if char not in counts:
          # return false because cannot be anagram
          return False
        # check if it is in the counts hash
        else:
          # decrement value by 1 for key of char to count it
          counts[char] -= 1
      
      # check if counts hash has 0 values so t is anagram of s
      return all(value == 0 for value in counts.values())
        