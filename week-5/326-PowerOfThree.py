def isPowerOfThreeRecursive(n):
    if n < 3:
        if n == 1:
            return True
        return False

    if n % 3 != 0:
        return False

    if n == 3:
        return True
    return isPowerOfThree(n / 3)


def isPowerOfThree(n):
    if n <= 0:
        return False
    log3 = math.log10(3)
    return math.log10(n)/log3 == math.floor(math.log10(n)/log3)
