class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Remove leading whitespaces
        s = s.lstrip()

        # Initialize variables
        sign = 1
        result = 0

        # Check for optional sign character
        if s and (s[0] == '+' or s[0] == '-'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        # Convert digits to integer
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        # Apply the sign
        result *= sign

        # Clamp the integer to the 32-bit signed integer range
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX

        return result