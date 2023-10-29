

def minPlanks(planks, k):
    _sum = float("inf")
    index = 0
    total = 0

    left = 0
    for i in range(len(planks)):
        total += planks[i]
        if i - left + 1 >= k:
            while i - left + 1 > k:
                total -= planks[left]
                left += 1
            if total < _sum:
                _sum = total
                index = left + 1

    return index


def main():

    n, k = list(map(int, input().split()))
    planks = list(map(int, input().split()))
    print(minPlanks(planks, k))


main()
