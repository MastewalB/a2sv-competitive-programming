import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(map(int, input().split()))


def main(n, k):
    available = 240 - k
    total = 0
    for i in range(1, n + 1):
        total += (5 * i)
        if total > available:
            return i - 1
    return i


if __name__ == "__main__":
    n, k = inlt()
    print(main(n, k))
