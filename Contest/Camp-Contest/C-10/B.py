s = input()
i = 0

lower = [0] * len(s)
upper = [0] * len(s)
while i < len(s):
    if s[i].isupper():
        upper[i] += 1
    else:
        lower[i] += 1

    if i > 0:
        lower[i] += lower[i - 1]
        upper[i] += upper[i - 1]
    i += 1
res = float("inf")
if upper[-1] == 0 or lower[-1] == 0:
    print(0)
    exit()
for i in range(len(s)):
    up = upper[-1] - upper[i] if s[i].isupper() else upper[-1] - 1
    res = min(up + lower[i], res)
print(res) if res != float("inf") else print(0)
