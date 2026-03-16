class Solution:
    # time: O(2^n) — worst case every substring is a valid word
    # space: O(n) — recursion depth and curr_words list
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
      # convert the list to set for O(1) lookup
      word_dict = set(wordDict)

      # i is the position in s to find the next word from
      def backtrack(i):
        # base case if i reached the end of s
        if i == len(s):
          # join all words with spaces and add to result
          result.append(" ".join(curr_words))
          return
        # try every subtring until the end of s
        for j in range(i, len(s)):
          # create the substrings
          word = s[i:j+1]

          # check if the substring is a valid dictionary word
          if word in word_dict:
            curr_words.append(word) # add substring to current path
            backtrack(j + 1)        # recursive check substrings from end of substring
            curr_words.pop()        # remove substring when coming back to try others
      
      # current path of substrings being built
      curr_words = []
      # valid sentences from substrings
      result = []
      # start the algorithm backtracking from position 0
      backtrack(0)
      return result
        