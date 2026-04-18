class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer limits
        MAX_INT = 2147483647  # 2^31 - 1
        MIN_INT = -2147483648 # -2^31

        # Handle overflow case mentioned in constraints
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine the sign of the result
        # If signs are different, result is negative
        is_negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0

        # Bit manipulation loop
        while a >= b:
            temp_divisor, count = b, 1
            # Keep shifting left (doubling) until temp_divisor > a
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            
            # Subtract the largest power-of-two multiple found
            a -= temp_divisor
            quotient += count

        # Apply the sign and stay within 32-bit bounds
        if is_negative:
            quotient = -quotient
            
        return max(MIN_INT, min(MAX_INT, quotient))