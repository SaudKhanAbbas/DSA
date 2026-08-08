# LeetCode 881. Boats to Save People

def numRescueBoats(people, limit):
    people.sort()
    l, r = 0, len(people) - 1
    boats = 0

    while l <= r:
        boats += 1

        if people[l] + people[r] <= limit:
            l += 1

        r -= 1

    return boats


# Pattern:
# Two Pointers + Greedy

# Time Complexity:
# O(n log n)
#
# - Sorting takes O(n log n).
# - The two-pointer traversal takes O(n).
# - Overall: O(n log n).

# Space Complexity:
# O(1)
#
# - Only a constant number of variables are used.
