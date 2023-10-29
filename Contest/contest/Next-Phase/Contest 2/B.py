import sys


def same_diagonal(ax, ay, cx, cy):
    return ax + ay == cx + cy or abs(cx - ax) == abs(cy - ay)


def same_row(ax, cx):
    return ax == cx


def same_col(ay, cy):
    return ay == cy


def in_bound(n, px, py):
    return 0 <= px < n and 0 <= py < n


def can_win(n, a, b, c):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    visited = set([(b[0], b[1])])

    def check(px, py):
        nonlocal a, c

        if px == c[0] and py == c[1]:
            return True

        ans = False
        for x, y in directions:
            n_x, n_y = px + x, py + y
            if in_bound(n, n_x, n_y) and (n_x, n_y) not in visited and not same_diagonal(a[0], a[1], n_x, n_y) and not same_col(a[1], n_y) and not same_row(a[0],  n_x):
                visited.add((n_x, n_y))
                res = check(n_x, n_y)
                if res:
                    ans = res
                    break

        return ans
    return "Yes" if check(b[0], b[1]) else "No"


sys.setrecursionlimit(10000)

n = int(input())
a = b = c = None
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

print(can_win(n, a, b, c))
