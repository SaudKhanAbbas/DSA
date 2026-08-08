# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = best = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            best = max(best, right - left + 1)

        return best

# Pattern: Sliding Window + Hash Set
# Time Complexity: O(n)
# Space Complexity: O(min(n, k))
