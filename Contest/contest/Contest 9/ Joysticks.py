from functools import lru_cache


def iterative(n, m):
    n, m = min(n, m), max(n, m)
    count = 0

    while n > 0 and m > 1:
        count += 1
        n += 1
        m -= 2
        n, m = min(n, m), max(n, m)
    return count


def joysticks(n, m):

    @lru_cache(None)
    def joy(n, m):
        if n <= 0 or m <= 0:
            return 0
        if n <= 1 and m <= 1:
            return 0
        return 1 + max(joy(n + 1, m - 2), joy(n - 2, m + 1))

    return joy(n, m)


def main():
    n, m = list(map(int, input().split()))
    print(iterative(n, m))


if __name__ == "__main__":
    main()
