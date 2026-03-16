class Solution:
    # time: O(m+n) 
    # space: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index of nums1
        p_insert = m + n - 1
        # last index of m nums1 integers
        p1 = m - 1
        # last index of n nums2 integers
        p2 = n - 1

        # merge in reverse order while both have elements
        while p1 >= 0 and p2 >= 0:  # >= not > so we include index 0
            if nums2[p2] >= nums1[p1]: # if the nums2 integer >= nums1 integer
                nums1[p_insert] = nums2[p2] # insert the nums2 integer into 0
                p2 -= 1 # check the next nums2 integer
            else: # if the nums2 integer < nums1 integer
                nums1[p_insert] = nums1[p1] # insert the nums1 integer into 0
                p1 -= 1 # check the next nums1 integer
            p_insert -= 1  # always move insert pointer back

        # if all the elements in nums1 are bigger
        # so nums2 still has elements then copy them over
        while p2 >= 0:
            nums1[p_insert] = nums2[p2]
            p2 -= 1
            p_insert -= 1
          
     
        
        
        