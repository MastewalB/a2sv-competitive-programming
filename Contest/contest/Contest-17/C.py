def playOptimally(col, path):
    bobScore = float("inf")

    for i in range(col - 1, 0, -1):
        path[0][i] += path[0][i + 1]
        path[1][i] += path[1][i + 1]
    for i in range(1, col + 1):
        bobScore = min(bobScore, max(
            path[0][i + 1], path[1][1] - path[1][i]))
    return bobScore


t = int(input())
for _ in range(t):
    col = int(input())
    path = [[0], [0]]
    for i in range(2):
        path[i].extend(list(map(int, input().split())))
        path[i].append(0)
    print(playOptimally(col, path))
