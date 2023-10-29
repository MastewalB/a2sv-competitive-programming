from collections import defaultdict


def tsum(arr):
    count = defaultdict(int)
    for num in arr:
        a = num % 10
        for i in range(10):
            if count[i] > 0:
                count[i] -= 1
                for j in range(10):
                    if count[j] > 0:
                        count[j] -= 1
                        if a + i + j == 3 or a + i + j == 13 or a + i + j == 23:
                            return "YES"
                        count[j] += 1
                count[i] += 1
        count[a] += 1

    return "NO"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(tsum(arr))


main()
