n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = set(x[1:])
y = set(y[1:])

x.update(y)


# if all(map(ismember, list(range(1, n + 1)))):
if len(x) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
