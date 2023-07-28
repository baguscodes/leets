class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define the Roman numeral symbols and their corresponding values
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        # Initialize the result to store the final integer value
        result = 0

        # Iterate through the Roman numeral string
        for i in range(len(s)):
            current_value = roman_values[s[i]]

            # If the current value is less than the next value, subtract it
            if i + 1 < len(s) and roman_values[s[i + 1]] > current_value:
                result -= current_value
            else:
                result += current_value

        return result