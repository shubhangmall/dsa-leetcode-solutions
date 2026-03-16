class Solution:
    # time: O(n) - right pointer moves n times
    # space: O(n) - hash set can store n unique chars from s
    def lengthOfLongestSubstring(self, s: str) -> int:
        # get the total length of the string s
        n = len(s)
        # track the longest substring window length
        max_length = 0
        # use hash set to check for repeating characters in window
        unique_chars = set()
        # use a pointer to start substring window at first char
        left = 0

        # use a pointer to end substring window at each char
        for right in range(n):
          # check if char is not repeating in substring window
          if s[right] not in unique_chars:
            # track the unique car in the hash set
            unique_chars.add(s[right])
            # calculate the current substring window length
            current_length = right - left + 1
            # update the tracker for longest substring window length
            max_length = max(max_length, current_length)
          # if char is repeating already in substring window
          else:
            # keep doing the below while it is repeating char
            while s[right] in unique_chars:
              # untrack the repeating char in the hash set
              unique_chars.remove(s[left])
              # start the substring window at the next char
              left += 1
            # once the char is not repeating track it in hash set
            unique_chars.add(s[right])
        
        # return the result
        return max_length
        