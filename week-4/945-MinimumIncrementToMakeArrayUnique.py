def minIncrementForUnique(nums):
    maximum_value = max(nums)
    count = collections.Counter(nums)
    duplicates = []

    moves = 0
    for x in range(len(nums) + maximum_value):
        if count[x] >= 2:
            duplicates.extend([x] * (count[x] - 1))
        elif duplicates and count[x] == 0:
            moves += x - duplicates.pop()

    return moves
