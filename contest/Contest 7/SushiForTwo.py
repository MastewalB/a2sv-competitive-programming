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


def main(n, sushi):
    max_length = 0
    current = sushi[0]
    previous_count = 0
    current_count = 0

    i = 0
    while i < len(sushi):
        if current == sushi[i]:
            current_count += 1

        else:
            current = sushi[i]
            max_length = max(
                max_length, 2 * min(current_count, previous_count))
            previous_count = current_count
            current_count = 1
        i += 1
    max_length = max(
        max_length, 2 * min(current_count, previous_count))
    return max_length


if __name__ == "__main__":
    n = inp()
    sushi = inlt()
    print(main(n, sushi))
