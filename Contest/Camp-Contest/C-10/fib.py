def generate(N):
    F = [1, 1]
    while F[-1] < N:
        F.append(F[-1] + F[-2])
    return set(F)


def fib(a):
    ans = [False] * len(a)
    fibSeq = generate(max(a))

    for i in range(len(a)):
        num = a[i]
        if num == 2:
            ans[i] = True
        else:
            for j in fibSeq:
                if num - j in fibSeq:
                    ans[i] = True
                    break

    return ans
