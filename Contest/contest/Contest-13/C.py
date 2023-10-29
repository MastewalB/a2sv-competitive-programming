def jump(array):
    array = " " + array
    n = len(array)
    prev, maxDiff = 0, 0

    for i in range(1, n):
        if array[i] == 'R':
            maxDiff = max(maxDiff, i - prev)
            prev = i
    maxDiff = max(maxDiff, n - prev)
    return maxDiff


t = int(input())
for _ in range(t):
    array = input().strip()
    print(jump(array))
