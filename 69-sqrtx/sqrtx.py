class Solution:
    def mySqrt(self, x: int) -> int:
        # Handle 0 and 1 separately
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            
            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # After the loop, 'right' is the floor of the square root
        return right