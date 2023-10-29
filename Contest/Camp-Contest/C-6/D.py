

def main():
    n, m, k = list(map(int, input().split()))

    def kthLargest(n, m, k):
        table = [[i for i in range(1, m + 1)] for _ in range(n)]
        # print(table)
        return

    print(kthLargest(n, m, k))


main()
