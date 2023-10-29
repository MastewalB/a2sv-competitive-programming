def find(x, arr):
    if x == len(arr):
        return -1
    while arr[x] != x and arr[x] != -1:
        arr[x] = arr[arr[x]]
        x = arr[x]
    return arr[x]


def solution(n, m, queries):

    rows = [i for i in range(n)]
    cols = [i for i in range(m)]

    minRow = minCol = 0
    res = []

    for query in queries:
        if query[0] == 0:
            val = n * (minRow) + minCol
            res.append(val)
        elif query[0] == 1:
            x = query[1]
            rows[x] = find(x + 1, rows)
            if x == minRow:
                minRow = rows[x]
        else:
            x = query[1]
            cols[x] = find(x + 1, cols)
            if x == minCol:
                minCol = cols[x]

    return res
