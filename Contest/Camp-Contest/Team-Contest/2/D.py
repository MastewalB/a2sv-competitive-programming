from collections import defaultdict, Counter


def minBox(A):
    freq = Counter(A)
    return max(freq.values())


def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(minBox(A))


main()
