# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set to store characters currently in the sliding window
        seen = set()

        # Left pointer and maximum length found so far
        left = best = 0

        # Expand the sliding window using the right pointer
        for right in range(len(s)):

            # If the current character already exists,
            # shrink the window from the left until it's removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add the current character to the window
            seen.add(s[right])

            # Calculate the current window length
            window_length = right - left + 1

            # Update the maximum length if needed
            if window_length > best:
                best = window_length

        return best


# Time Complexity:
# O(n)
# - Each character is added to the set at most once.
# - Each character is removed from the set at most once.
# - Both pointers traverse the string only once.
# Overall = O(n)

# Space Complexity:
# O(min(n, k))
# - 'seen' stores at most one occurrence of each character
#   in the current window.
# - k = size of the character set.
# - Worst case: O(n) if all characters are unique.
```
