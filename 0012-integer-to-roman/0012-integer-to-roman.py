class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define the Roman numeral symbols and their corresponding values
        roman_symbols = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]

        roman_numeral = ""
        for symbol, value in roman_symbols:
            while num >= value:
                roman_numeral += symbol
                num -= value

        return roman_numeral
