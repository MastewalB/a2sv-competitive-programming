from collections import defaultdict


def solve(pairs):
    count_parents = defaultdict(int)

    for parent, child in pairs:
        count_parents[child] += 1
        count_parents[parent]

    zero = []
    one = []
    for k, v in count_parents.items():
        if v == 0:
            zero.append(k)
        if v == 1:
            one.append(k)

    return


P = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4), (13, 20)
]

solve(pairs=P)
