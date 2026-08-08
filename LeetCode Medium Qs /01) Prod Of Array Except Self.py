# LeetCode 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize prefix, suffix, and result arrays
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        # Build prefix product array
        # prefix[i] = product of all elements before index i
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Build suffix product array
        # suffix[i] = product of all elements after index i
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Multiply prefix and suffix products
        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result


# Pattern:
# Prefix & Suffix Product Pattern

# Time Complexity:
# O(n)
#
# - One pass to build the prefix array.
# - One pass to build the suffix array.
# - One pass to compute the result.
#
# Total = O(n)

# Space Complexity:
# O(n)
#
# - Prefix array: O(n)
# - Suffix array: O(n)
# - Result array: O(n)
#
# Overall auxiliary space = O(n)
