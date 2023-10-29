def binarySearch(info, target):
    left = 0
    right = len(info) - 1
    while left < right:
        mid = (left + right) >> 1
        if info[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left 

def goodTopics(n, a, b):
    total = 0
    info = []
    for i in range(n):
        info.append(b[i] - a[i])
    info.sort()

    for i in range(n):
        target = a[i] - b[i] 
        index = binarySearch(info, target)
        print(index)
        total += index
    print(total)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
goodTopics(n, a, b)