class Solution:
    # time: O(log x) — binary search cuts range in half each step
    # space: O(1) — only using a few variables
    def mySqrt(self, x: int) -> int:
        # left boundary starts at 0
        left = 0
        # right boundary starts at x
        right = x
        # track the best valid result found so far
        result = 0

        # keep searching while boundaries have not crossed
        while left <= right:
            # calculate the distance between boundaries
            half_way = (right - left) // 2
            # calculate the middle index
            middle = left + half_way
            # check if middle squared is too big
            if middle**2 > x:
                # move right boundary down
                right = middle - 1
            # check if middle squared is too small
            elif middle**2 < x:
                # move left boundary up
                left = middle + 1
                # update result to current middle — best valid floor so far
                result = middle
            # middle squared equals x exactly
            else:
                # perfect square found — return middle
                return middle

        # return the floor of sqrt(x)
        return result