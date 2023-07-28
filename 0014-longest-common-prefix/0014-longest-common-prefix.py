class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Iterate through the characters of the first string
        for i, char in enumerate(strs[0]):
            # Compare the character with the corresponding characters in other strings
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return strs[0][:i]

        return strs[0]