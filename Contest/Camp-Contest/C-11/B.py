def check(N, M):
    count = 0
    if len(str(N)) == len(str(M)):
        if len(str(N)) == 1:
            return True
        while N > 0 and M > 0:
            count += (N % 10) == (M % 10)
            N //= 10
            M //= 10
    return count


def div7(N):
    rem = N % 7
    if rem == 0 and N < 10:
        print(7)
        return
    possible = [N - rem, N + 7 - rem]
    for num in possible:
        C = check(N, num)
        if C:
            print(num)
            break


def main():
    t = int(input())
    for _ in range(t):
        N = int(input())
        div7(N)


main()
