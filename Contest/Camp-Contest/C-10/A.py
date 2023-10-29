def max_val(l, r, a):
    p = r - (r % a)
    q = (r // a) + (r % a)
    if l <= p <= r:
        if l <= p - 1 <= r:
            m = (p - 1) // a + (p - 1) % a
            return max(p // a, m, q)
        return max(p // a, q)

    return q


t = int(input())
for _ in range(t):
    l, r, a = list(map(int, input().split()))
    print(max_val(l, r, a))
