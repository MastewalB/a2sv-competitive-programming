def isPowerOfFour(n):
    if n <= 0:
        return False
    log4 = math.log10(4)
    return math.log10(n)/log4 == math.floor(math.log10(n)/log4)


# 15min
