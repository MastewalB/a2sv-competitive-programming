
def toAdd(array, N, k):
    array.sort()
    currSum, left = 0, 0
    freq = 1
    elemIndex = 0

    for i in range(N):
        currSum += array[i]
        while currSum + k < array[i] * (i - left + 1) and left <= i:
            currSum -= array[left]
            left += 1
        if i - left + 1 > freq:
            freq = i - left + 1
            elemIndex = i

    return [freq, array[elemIndex]]


def main():
    n, k = list(map(int, input().split()))
    array = list(map(int, input().split()))
    print(*toAdd(array, n, k))


main()
