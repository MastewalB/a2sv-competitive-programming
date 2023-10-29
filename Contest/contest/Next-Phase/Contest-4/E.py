def count(array, k, n):
    count = 0

    left = 0
    for i in range(n):
        if i > 0 and array[i] * 2 <= array[i - 1]:
            left = i
        if i - left == k:
            count += 1
            left += 1

    return count


t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    array = list(map(int, input().split()))
    print(count(array, k, n))
