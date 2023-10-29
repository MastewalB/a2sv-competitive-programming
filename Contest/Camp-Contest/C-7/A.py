
def minCandies(candies):
    _min = min(candies)
    total = 0

    for candy in candies:
        total += candy - _min
    return total


def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        candies = list(map(int, input().split()))
        print(minCandies(candies))


main()
