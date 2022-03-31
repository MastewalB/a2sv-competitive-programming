import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return(int(input()))


def main(target):
    a, b = 31, 32
    for t in target:
        d_a, d_b = t - 31, t - 32

        if d_a % 4 == 0:
            print(a)
            continue
        if d_b % 4 == 0:
            print(b)
            continue

        if (4 - d_a % 4) < (4 - d_b % 4):
            print(a)
            continue
        else:
            print(b)
            continue


if __name__ == "__main__":
    n = inp()
    target = []
    for _ in range(n):
        target.append(inp())
    main(target)
