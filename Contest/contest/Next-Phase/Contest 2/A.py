def make_even(N):

    if int(N[-1]) % 2 == 0:
        return 0
    if int(N[0]) % 2 == 0:
        return 1
    for i in range(len(N)):
        if int(N[i]) % 2 == 0:
            return 2
    return -1


t = int(input())
for _ in range(t):
    print(make_even(input()))
