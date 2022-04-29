import sys
input = sys.stdin.readline


def inp():
    return int(input())


def inlt():
    return list(map(int, input().split()))


def powerWalk(k, powerUps):
    hasSeen = set(powerUps)
    for i in range(1, k + 1):
        print(max(i, len(hasSeen)), end=" ")
    print()


if __name__ == "__main__":
    n = inp()
    for _ in range(n):
        k = inp()
        powerUps = inlt()
        powerWalk(k, powerUps)
