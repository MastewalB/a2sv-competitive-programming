def canConvert(a, b):

    max_moves = -1
    max_zero = -1
    for i in range(len(a)):
        if a[i] < b[i]:
            return "NO"
        max_moves = max(max_moves, a[i] - b[i])
    for i in range(len(a)):
        if a[i] - b[i] <= max_moves:
            if a[i] - b[i] < max_moves and b[i] != 0:
                return "NO"
        else:
            return "NO"

    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(canConvert(a, b))
