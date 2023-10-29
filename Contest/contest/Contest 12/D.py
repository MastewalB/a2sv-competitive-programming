def word(s):
    f = [0] * len(s)

    def failure(s):
        i = 1
        j = 0

        while i < len(s):
            if s[i] == s[j]:
                f[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = f[j - 1]
            else:
                f[i] = 0
                i += 1
    failure(s)
    # print(f)
    if s[0:f[-1]] in s[f[-1]:-f[-1]]:
        print(s[0:f[-1]])
    else:
        print("Just a legend")


s = input()
word(s)
