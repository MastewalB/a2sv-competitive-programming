def loveTriangle(planes):
    for i in range(1, len(planes)):
        if i == planes[planes[planes[i]]]:
            return "YES"

    return "NO"


n = int(input())
planes = [0] + list(map(int, input().split()))
print(loveTriangle(planes))
