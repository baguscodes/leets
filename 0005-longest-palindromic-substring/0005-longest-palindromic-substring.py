class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome with s[i] as center
            palindrome1 = expand_around_center(i, i)
            # Even-length palindrome with s[i] and s[i+1] as centers
            palindrome2 = expand_around_center(i, i + 1)

            # Update longest palindrome found so far
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2

        return longest
