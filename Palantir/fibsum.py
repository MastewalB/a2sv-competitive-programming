def generate(N):
    a, b = 1, 2
    fibs = set([a, b])
    while b <= N:
        fibs.add(b)
        a, b = b, a + b
    return fibs


def fib_sum(a):
    _max = max(a)
    fibs = generate(_max)
    ans = [False] * len(a)
    for j in range(len(a)):
        n = a[j]
        for i in fibs:
            if n - i in fibs:
                ans[j] = True
                break
            if i > n:
                break
    return ans


a = [2, 5, 17]
print(fib_sum(a))
