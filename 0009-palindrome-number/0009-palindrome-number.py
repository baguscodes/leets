class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even-length numbers, x and reversed_half will be equal.
        # For odd-length numbers, x will be one digit less than reversed_half.
        return x == reversed_half or x == reversed_half // 10