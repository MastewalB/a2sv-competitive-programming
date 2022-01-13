def minNonZeroProduct(p):
    mod = pow(10, 9) + 7
    target = pow(2, p, mod)
    exp = pow(2, p - 1) - 1
    return (pow(target - 2, exp, mod) * (target - 1)) % mod


p = 20
print(minNonZeroProduct(p))
