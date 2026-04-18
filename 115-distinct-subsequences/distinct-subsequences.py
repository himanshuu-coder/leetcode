class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # Create a 2D DP table initialized with 0
        # dp[i][j] is the number of ways to form t[:j] using s[:i]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty t can be formed by any prefix of s in 1 way
        for i in range(m + 1):
            dp[i][0] = 1
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, we sum the two choices (take or leave)
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    # If characters don't match, we must leave the current s[i-1]
                    dp[i][j] = dp[i-1][j]
                    
        return dp[m][n] 