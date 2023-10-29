n = list(input())

for i in range(len(n)):
    if i == 0 and 5 <= int(n[i]) < 9 or i > 0 and 5 <= int(n[i]) <= 9:
        n[i] = str(9 - int(n[i]))

n = ''.join(n)
print(int(n))
