from collections import defaultdict, deque
import heapq


def the_way_home(s, n, d):

    queue = deque([0])
    jumps = 0
    path = 0
    prev = None
    ans = []

    while path < n - 1:
        if ans and path == ans[-1]:
            break
        ans.append(path)
        for j in range(d, 0, -1):
            if path + j < n and s[path + j] == '1':
                path += j
                break
    if ans and n - 1 - ans[-1] > d:
        return -1
    # print(ans)
    return len(ans)


n, d = list(map(int, input().split()))
s = input()
print(the_way_home(s, n, d))
