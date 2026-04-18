class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # 'i' is the pointer for the last unique element found
        i = 0
        
        # 'j' scans the rest of the array
        for j in range(1, len(nums)):
            # If we find a new unique element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # The number of unique elements is i + 1 (since i is an index)
        return i + 1