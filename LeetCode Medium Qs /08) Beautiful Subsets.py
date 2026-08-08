# LeetCode 2597. The Number of Beautiful Subsets

from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = defaultdict(int)

        def dfs(i):
            if i == len(nums):
                return 1

            ans = dfs(i + 1)

            if count[nums[i] - k] == 0:
                count[nums[i]] += 1
                ans += dfs(i + 1)
                count[nums[i]] -= 1

            return ans

        return dfs(0) - 1


# Pattern:
# Backtracking / DFS + Frequency Hash Map

# Time Complexity:
# O(2^n)

# Space Complexity:
# O(n)
