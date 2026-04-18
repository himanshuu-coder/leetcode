class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set pointers for the end of valid elements in both arrays
        p1 = m - 1
        p2 = n - 1
        # Set pointer for the very end of nums1
        p = m + n - 1
        
        # While there are elements to compare in both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # If nums2 still has elements, copy them (nums1 elements are already there)
        # This covers cases like nums1 = [0], m = 0, nums2 = [1], n = 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1