
def changeBit(N):
    return list(map(int, (bin(N))[2:]))


def maxxor(l, d):
    l_bit, d_bit = changeBit(l), changeBit(d)
    current_l, current_d = l, d

    diff = len(d_bit) - len(l_bit)
    l_bit = ([0] * diff) + l_bit
    N = len(l_bit)

    for i in range(N):

        if l_bit[i] == d_bit[i]:
            if d_bit[i] == 1 and current_d - pow(2, N - i - 1) >= l:
                current_d -= pow(2, N - i - 1)

            elif l_bit[i] == 0 and current_l + pow(2, N - i - 1) <= d:
                current_l += pow(2, N - i - 1)

    return current_l ^ current_d


def main():
    l, d = list(map(int, input().split()))
    print(maxxor(l, d))


main()
