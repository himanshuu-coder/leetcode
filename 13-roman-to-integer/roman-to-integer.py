class Solution:
    def romanToInt(self, s: str) -> int:
        # Step 1: Create the mapping of Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Step 2: Iterate through the string
        for i in range(n):
            current_val = roman_map[s[i]]
            
            # Step 3: Check if we are at the last character or if 
            # the current value is less than the next value
            if i < n - 1 and current_val < roman_map[s[i + 1]]:
                total -= current_val
            else:
                total += current_val
                
        return total