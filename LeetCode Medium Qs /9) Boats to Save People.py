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

# Time Complexity: O(n log n)
# Space Complexity: O(1)
