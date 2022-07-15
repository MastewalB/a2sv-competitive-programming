n = int(input())
array = list(map(int, input().split()))

longest = 1
curr = 1
for i in range(1, n):
    if array[i - 1] >= array[i]:
        curr = 0
    curr += 1
    longest = max(longest, curr)
print(longest)
