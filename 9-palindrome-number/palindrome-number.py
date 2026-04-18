class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge Case: Negative numbers and numbers ending in 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            # Get the last digit and add it to the reversed half
            reversed_half = (reversed_half * 10) + (x % 10)
            # Remove the last digit from x
            x //= 10
            
        # For even-length numbers: x == reversed_half
        # For odd-length numbers: x == reversed_half // 10 (removes the middle digit)
        return x == reversed_half or x == reversed_half // 10