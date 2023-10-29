def maxBooks(books, t):
    # for i in range(1, len(books)):
    #     books[i] += books[i - 1]

    j = 0
    curr = 0
    _max = 0
    for i in range(len(books)):
        curr += books[i]
        while j <= i and curr > t:
            curr -= books[j]
            j += 1

        _max = max(_max, i - j + 1)

    return _max


n, t = list(map(int, input().split()))
books = list(map(int, input().split()))
print(maxBooks(books, t))
