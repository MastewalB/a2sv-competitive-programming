import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def invr():
    return(map(int, input().split()))


def countDamage(k, attacks):
    total = k
    for i in range(len(attacks) - 1):
        total += min(k, attacks[i + 1] - attacks[i])
    return total


def main(h, attacks):
    left, right = 1, h

    while left <= right:
        mid = (left + right) // 2
        damage = countDamage(mid, attacks)

        if damage == h:
            return mid
        if damage > h:
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    tests = inp()
    for _ in range(tests):
        _, h = inlt()
        attacks = inlt()
        print(main(h, attacks))
