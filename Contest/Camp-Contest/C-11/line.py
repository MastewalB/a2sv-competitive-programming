from collections import defaultdict


def oneLight(lamps):
    coordinate = defaultdict(int)

    for center, radius in lamps:
        left = center - radius
        right = center + radius + 1
        coordinate[left] += 1
        coordinate[right] -= 1

    C = list(coordinate.keys())
    C.sort()
    freq = 0
    count = 0
    for i in range(len(C)):
        if freq == 1:
            if i == 0:
                count += 1
            else:
                count += C[i] - C[i - 1]
        freq += coordinate[C[i]]

    return count


lamps = [[-2, 3], [2, 3], [2, 1]]
lamps = [[10000000000, 1000000]]
print(oneLight(lamps))
