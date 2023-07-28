class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def get_factorial(num):
            # Calculate the factorial of a number
            if num == 0 or num == 1:
                return 1
            return num * get_factorial(num - 1)

        k -= 1  # Convert k to 0-indexed

        used = [False] * n
        result = ""

        for i in range(n, 0, -1):
            fact = get_factorial(i - 1)
            index = k // fact
            k %= fact

            count = 0
            for j in range(n):
                if not used[j]:
                    count += 1
                    if count == index + 1:
                        result += str(j + 1)
                        used[j] = True
                        break

        return result