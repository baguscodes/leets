class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Find the shortest string in the list (since the common prefix cannot be longer)
        shortest_str = min(strs, key=len)

        # Iterate through the characters of the shortest string
        for i, char in enumerate(shortest_str):
            # Compare the character with the corresponding characters in other strings
            for string in strs:
                if string[i] != char:
                    return shortest_str[:i]

        return shortest_str
