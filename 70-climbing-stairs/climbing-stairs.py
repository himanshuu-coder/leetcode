class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        if n <= 2:
            return n
        
        # We only need to keep track of the two previous steps
        first = 1  # Ways to reach step 1
        second = 2 # Ways to reach step 2
        
        for i in range(3, n + 1):
            current = first + second
            # Update pointers for the next iteration
            first = second
            second = current
            
        return second