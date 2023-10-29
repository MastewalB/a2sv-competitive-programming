def binDeq(s, array):

    l = 0
    longest = 0
    running = 0
    for i in range(len(array)):
        running += array[i]

        while running >= s:
            longest = max(longest, i - l + 1)
            running -= array[l]
            l += 1

    return len(array) - longest if longest else -1


t = int(input())
for _ in range(t):
    n, s = list(map(int, input().split()))
    array = list(map(int, input().split()))
    print(binDeq(s, array))
