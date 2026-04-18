class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Take the first string as a reference
        first_word = strs[0]
        
        for i in range(len(first_word)):
            char = first_word[i]
            
            # Compare this character with the same index in all other strings
            for j in range(1, len(strs)):
                # If index i is out of bounds for strs[j] or characters don't match
                if i == len(strs[j]) or strs[j][i] != char:
                    return first_word[:i]
        
        return first_word