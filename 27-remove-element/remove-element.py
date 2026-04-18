class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # 'k' tracks the position for elements not equal to val
        k = 0
        
        for i in range(len(nums)):
            # If the current element is not the value we want to remove
            if nums[i] != val:
                # Move it to the 'k' position and increment k
                nums[k] = nums[i]
                k += 1
        
        # k is now the count of elements that are not 'val'
        return k