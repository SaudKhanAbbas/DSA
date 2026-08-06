def count_subarrays(nums, left, right):
    def count(limit):
        total = 0
        length = 0

        for num in nums:
            if num <= limit:
                length += 1
            else:
                length = 0
            total += length

        return total

    return count(right) - count(left - 1)

# Time Complexity: O(n)
# - The helper function `count()` traverses the array once (O(n)).
# - It is called twice, so the total is O(2n), which simplifies to O(n).

# Space Complexity: O(1)
# - Only a few variables (`total`, `length`, and `limit`) are used.
# - No extra data structures proportional to the input size are allocated.
