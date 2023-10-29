
def backwards(s, p):

    i = len(s) - 1
    j = len(p) - 1

    while i >= 0 and j >= 0 and s[i] == p[j]:
        i -= 1
        j -= 1

    return i + j + 2


p = input()
s = input()
print(backwards(s, p))
