output = 0

n = int(input())
for _ in range(n):
    problem = list(map(int, input().split(" ")))
    one = 0
    for i in range(len(problem)):
        if problem[i] == 1:
            one += 1
    if one > 1:
        output += 1
print(output)
