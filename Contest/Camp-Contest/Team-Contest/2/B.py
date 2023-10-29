from collections import defaultdict


def same(A):
    count = defaultdict(int)
    for i, n in enumerate(A):
        count[n - i] += 1

    # print(count.values())
    ans = 0
    for a in count.values():
        if a == 2:
            ans += 1
        elif a > 2:
            ans += (a // 2) * (a - 1) if a % 2 == 0 else (a // 2) * a
    return ans


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        print(same(A))


main()
