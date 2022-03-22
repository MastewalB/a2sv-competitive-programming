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


def main(n, shops, coins):
    shops.sort()
    for i in range(len(coins)):
        left = 0
        right = len(shops) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if coins[i] >= shops[mid]:
                left = mid + 1
            else:
                right = mid - 1
        print(left)


if __name__ == "__main__":
    n = inp()
    shops = inlt()
    q = inp()
    coins = []
    for _ in range(q):
        coins.append(inp())
    main(n, shops, coins)
