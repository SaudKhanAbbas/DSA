# 15. 3Sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to use the two-pointer technique
        nums.sort()
        result = []

        # Choose the first element of the triplet
        for i in range(len(nums) - 2):

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # Found a valid triplet
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # Sum is too small, move left pointer to increase the sum
                elif current_sum < 0:
                    left += 1

                # Sum is too large, move right pointer to decrease the sum
                else:
                    right -= 1

        return result


# Time Complexity:
# O(n²)
# - Sorting the array takes O(n log n).
# - The outer loop runs O(n) times.
# - The two-pointer scan runs O(n) in total for each iteration.
# Overall = O(n²)

# Space Complexity:
# O(1) auxiliary space
# - The algorithm uses only a few extra variables.
# - The output list is not counted toward auxiliary space.
#
# Note:
# Python's built-in sort() uses O(log n) stack space internally.
