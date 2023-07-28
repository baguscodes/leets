class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(num):
            # Calculate the factorial of a number
            if num == 0 or num == 1:
                return 1
            return num * factorial(num - 1)

        # Create a list of numbers from 1 to n
        numbers = list(range(1, n + 1))

        # Initialize the result string
        result = ""

        # Convert k to 0-indexed
        k -= 1

        # Iterate through the numbers from n to 1
        for i in range(n, 0, -1):
            # Calculate the index of the number to use from the numbers list
            index = k // factorial(i - 1)
            # Append the selected number to the result
            result += str(numbers[index])
            # Remove the selected number from the numbers list
            numbers.pop(index)
            # Update k to find the next number
            k %= factorial(i - 1)

        return result
