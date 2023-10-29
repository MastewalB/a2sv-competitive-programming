
def good_sum(a, s):
    x = 0
    L = 0
    longest = 0
    for i in range(len(a)):
        x += a[i]
        while x > s:
            x -= a[L]
            L += 1
        longest = max(longest, i - L + 1)

    return longest


n, s = list(map(int, input().split()))
a = list(map(int, input().split()))
print(good_sum(a, s))
