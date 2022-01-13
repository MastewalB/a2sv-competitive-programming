def countGoodNumbers(n):
    even = math.ceil(n / 2)
    odd = n - even
    mod = pow(10, 9) + 7
    return (pow(5, even, mod) * pow(4, odd, mod)) % mod
