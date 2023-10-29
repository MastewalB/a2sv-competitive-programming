import sys
input = sys.stdin.readline


def minCalories(calories, strip):
    total = 0
    for c in strip:
        c = int(c)
        total += calories[c - 1]
    return total


def main():
    calories = list(map(int, input().split()))
    strip = input().strip()
    print(minCalories(calories, strip))


main()
