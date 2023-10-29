
def maxSeq(A):
    B = C = 0
    for num in A:
        if num >= 0:
            B += num
        else:
            C += num

    return B - C


def main():
    n = int(input())
    A = list(map(int, input().split()))
    print(maxSeq(A))


main()
