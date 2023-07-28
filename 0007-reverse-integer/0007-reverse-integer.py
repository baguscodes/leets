class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit integer boundaries
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Initialize variables
        reversed_x = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        # Reverse the digits
        while x != 0:
            pop = x % 10
            x //= 10

            # Check for integer overflow
            if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and pop > 7):
                return 0

            reversed_x = reversed_x * 10 + pop

        # Apply the sign
        reversed_x *= sign

        # Check for integer overflow after applying the sign
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x
