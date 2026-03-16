class Solution:
  # time: O(log(n - k)) — binary search over range of size n-k where n is len(arr)
  # space: O(1) — only using a few variables
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
      # start window at index 0
      left = 0
      # end window at last index that fits k elements
      right = len(arr) - k

      # binary search loop
      while left < right:
        mid = (left + right) // 2

        # check if left candidate is farther from x
        if x - arr[mid] > arr[mid + k] - x:
          # start the window after left candidate
          left = mid + 1
        else:
          # right candidate is farther or equal from x
          # keep window or move left
          right = mid

      # when loop finishes left == right
      # so we get left to left + k elements from arr
      return arr[left:left+k]