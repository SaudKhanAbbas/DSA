class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0

            # Calculate total hours needed at speed = mid
            for pile in piles:
                hours += (pile + mid - 1) // mid   # Ceiling division

            if hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


# Time Complexity: O(n * log(max(piles)))
#   - Binary search over the range [1, max(piles)].
#   - For each candidate speed, iterate through all n piles.

# Space Complexity: O(1)
#   - Uses only a constant amount of extra space.
