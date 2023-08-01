class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array to use the two-pointer approach
        nums.sort()
        result = []

        # Iterate through the array using the first pointer (i)
        for i in range(len(nums) - 2):
            # Skip duplicates for the first element (i)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Set the second pointer (j) at the start and the third pointer (k) at the end
            j = i + 1
            k = len(nums) - 1

            # Perform two-pointer traversal
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    # Found a triplet with sum zero, add it to the result
                    result.append([nums[i], nums[j], nums[k]])

                    # Skip duplicates for the second pointer (j)
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    # Skip duplicates for the third pointer (k)
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    # Move both pointers inward
                    j += 1
                    k -= 1

        return result
