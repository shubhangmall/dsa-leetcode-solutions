class Solution:
    # time: O(n) to explore num int
    # space: O(n) for converting num to list
    def maximumSwap(self, num: int) -> int:
        # convert integer to list of digit characters
        num = list(str(num))

        # track the maximum digit seen so far scanning right to left
        max_digit = "0"
        # track the index of the maximum digit
        max_i = -1
        # track the left index of the best swap pair
        swap_i = -1
        # track the right index of the best swap pair
        swap_j = -1

        # scan right to left through all digits
        for i in reversed(range(len(num))):
            # get the current digit
            curr_digit = num[i]
            # check if current digit is larger than max seen so far
            if curr_digit > max_digit:
                # update max digit to current digit
                max_digit = curr_digit
                # update max index to current index
                max_i = i
            # check if current digit is smaller than max seen so far
            if curr_digit < max_digit:
                # record this as the best swap — leftmost digit with larger digit to its right
                swap_i, swap_j = i, max_i

        # swap the two digits to get maximum number
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        # convert digit list back to integer and return
        return int("".join(num))