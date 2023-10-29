n, h = list(map(int, input().split()))
minWidth = 0
heights = list(map(int, input().split()))
for i in range(n):
    if heights[i] > h:
        minWidth += 2
    else:
        minWidth += 1
print(minWidth)
