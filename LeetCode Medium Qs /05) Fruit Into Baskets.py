# LeetCode 904. Fruit Into Baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = ans = 0

        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            ans = max(ans, right - left + 1)

        return ans


# Pattern:
# Sliding Window + Hash Map / Frequency Map

# Time Complexity:
# O(n)
#
# - The right pointer traverses the array once.
# - The left pointer also traverses the array at most once.
# - Each element is added to and removed from the dictionary at most one time.

# Space Complexity:
# O(1)
#
# - The dictionary stores counts of at most 3 fruit types at any time
#   (before shrinking the window), which is constant extra space.
