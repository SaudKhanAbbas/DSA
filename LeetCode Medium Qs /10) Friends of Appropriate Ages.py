def numFriendRequests(ages):
    ages.sort()
    left = right = ans = 0

    for age in ages:
        if age < 15:
            continue

        while ages[left] <= age // 2 + 7:
            left += 1

        while right + 1 < len(ages) and ages[right + 1] <= age:
            right += 1

        ans += right - left

    return ans

# Time Complexity: O(n log n)
# Space Complexity: O(1)
