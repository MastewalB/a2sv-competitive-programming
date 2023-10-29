
def numberOfPossibilities(excluded):
    A = set(list(range(0, 10))) - excluded
    print(A)
    return


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        exclude = set(list(map(int, input().split())))
        print(numberOfPossibilities(exclude))


main()
