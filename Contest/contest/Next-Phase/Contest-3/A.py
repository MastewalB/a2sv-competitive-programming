def pos(polyNums):
    a = polyNums[0]

    for i in range(1, len(polyNums)):
        posSet = set(polyNums)
        posSet.remove(a)
        b = polyNums[i]
        if a + b in posSet:
            if b in posSet:
                posSet.remove(b)
            posSet.remove(a + b)
            for j in range(i + 1, len(polyNums)):
                c = polyNums[j]
                if a + b + c in posSet:
                    if c in posSet:
                        posSet.remove(c)
                    if a + c in posSet:
                        posSet.remove(a + c)
                    if b + c in posSet:
                        posSet.remove(b + c)
                    if a + b + c in posSet:
                        posSet.remove(a + b + c)
                    if len(posSet) == 0:
                        return [a, b, c]

    return


t = int(input())
for _ in range(t):
    polyNums = list(map(int, input().split()))
    print(*pos(polyNums))
