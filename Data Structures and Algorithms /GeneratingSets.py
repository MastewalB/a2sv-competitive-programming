import heapq


def generate(n, original):
    ans = set()
    for i in range(n):
        ans.add(original[i])
        original[i] *= -1

    heapq.heapify(original)
    while original:
        num = -heapq.heappop(original)
        ans.remove(num)

        p = num // 2
        while p > 0:
            if p not in ans:
                ans.add(p)
                heapq.heappush(original, -p)
                break
            else:
                p //= 2

        if p <= 0:
            ans.add(num)
            break
        ans.add(p)
    return ans


n = int(input())
original = list(map(int, input().split()))
print(*generate(n, original))
