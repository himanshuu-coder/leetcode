class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        # Continue as long as there are bits to process or a carry remains
        while i >= 0 or j >= 0 or carry:
            # Get the bit from 'a' if it exists, otherwise 0
            bit_a = int(a[i]) if i >= 0 else 0
            # Get the bit from 'b' if it exists, otherwise 0
            bit_b = int(b[j]) if j >= 0 else 0

            # Calculate the current sum and the carry
            total = bit_a + bit_b + carry
            res.append(str(total % 2))
            carry = total // 2

            # Move pointers to the left
            i -= 1
            j -= 1

        # Join the list and reverse it to get the final binary string
        return "".join(res[::-1])
         