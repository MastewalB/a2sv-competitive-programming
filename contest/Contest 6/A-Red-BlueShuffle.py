import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def insr():
    s = input()
    return(list(map(int, s[:len(s) - 1])))


def shuffle(n, red, blue):
    red_count, blue_count = 0, 0

    for i in range(n):
        if red[i] > blue[i]:
            red_count += 1
        elif red[i] < blue[i]:
            blue_count += 1

    if red_count > blue_count:
        print("RED")
    elif red_count < blue_count:
        print("BLUE")
    else:
        print("EQUAL")


if __name__ == "__main__":
    n = inp()
    for _ in range(n):
        cards = inp()
        red, blue = insr(), insr()
        shuffle(cards, red, blue)
