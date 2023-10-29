# https://codeforces.com/gym/407211

def check(arr, n):
    arr.sort()
    for i in range(1, n):
        if arr[i] - arr[i - 1] > 1:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(check(arr, n))
