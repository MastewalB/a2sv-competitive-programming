def longestUncommon(a, b):
    if a != b:
        return max(len(a), len(b))
    return -1


a = input()
b = input()
print(longestUncommon(a, b))
