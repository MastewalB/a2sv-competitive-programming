

def minVal(arr, n):
    And = arr[0]
    for i in range(1, n):
        And &= arr[i]

    return And


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(minVal(arr, n))


main()
