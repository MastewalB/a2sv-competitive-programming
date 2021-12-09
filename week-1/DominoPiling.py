inp = input()
a = inp.split(" ")
m = int(a[0])
n = int(a[1])


def domino_piling(m, n):
    return (m * n) // 2


print(domino_piling(m, n))
