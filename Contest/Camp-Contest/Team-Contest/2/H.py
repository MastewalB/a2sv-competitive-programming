
def password(s):
    if len(set(s)) == 1:
        if len(s) >= 3:
            print(s[0:len(s) // 3])
        else:
            print("Just a legend")
        return
    failure = [0] * len(s)
    i = 1
    j = 0

    while i < len(s):
        if s[i] == s[j]:
            failure[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = failure[j - 1]
        else:
            failure[i] = 0
            i += 1

    count = 0
    ptr = 0
    while ptr < len(s) and s[ptr] == 0:
        count += 1
        ptr += 1
    # print(failure)
    if (failure[-1] > len(s) - failure[-1] and failure[-1] % (len(s) - failure[-1]) == 0):
        print(s[0:len(s) // 3])
    elif s[0:failure[-1]] in s[failure[-1]:-failure[-1]]:
        print(s[0:failure[-1]])
    else:
        print("Just a legend")


def main():
    s = input()
    password(s)


main()
