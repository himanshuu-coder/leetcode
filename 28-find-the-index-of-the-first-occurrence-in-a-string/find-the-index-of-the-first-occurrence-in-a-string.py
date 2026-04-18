class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)

        # If needle is empty or longer than haystack, handle accordingly
        if n_len > h_len:
            return -1

        # Slide the window across the haystack
        for i in range(h_len - n_len + 1):
            # Check if the substring matches the needle
            if haystack[i : i + n_len] == needle:
                return i
        
        return -1    