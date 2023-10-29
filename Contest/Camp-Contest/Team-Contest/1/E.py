
def constanze(s):
    arr = [1] * (len(s) + 1)
    MOD = pow(10, 9) + 7
    for val in s:
        if val == 'm' or val == 'w':
            return 0
    for i in range(2, len(s) + 1):

        if s[i - 2:i] == 'nn' or s[i - 2:i] == 'uu':
            arr[i] = (arr[i - 1] + arr[i - 2]) % MOD
        else:
            arr[i] = arr[i - 1]

    return arr[len(s)]


def main():
    s = input()
    print(constanze(s))


main()
