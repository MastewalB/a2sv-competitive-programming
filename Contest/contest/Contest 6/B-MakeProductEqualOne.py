import sys
input = sys.stdin.readline


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def product(nums):
    neg_count, cost = 0, 0
    zero_count = 0

    for num in nums:
        if num > 0:
            cost += abs(num - 1)
        elif num == 0:
            cost += 1
            zero_count += 1
        else:
            cost += abs(num - (-1))
            neg_count += 1
    if neg_count % 2 != 0:
        if zero_count == 0:
            cost += 2
    return cost


if __name__ == "__main__":
    n = inp()
    nums = inlt()
    print(product(nums))
