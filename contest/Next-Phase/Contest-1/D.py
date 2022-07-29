from collections import defaultdict

vitamins = defaultdict(int)

t = int(input())
for _ in range(t):
    p, s = list(input().split())
    p = int(p)
    s = ''.join(sorted(s))

    if vitamins[s]:
        vitamins[s] = min(vitamins[s], p)
    else:
        vitamins[s] = p

minPrice = float('inf')
flag = 0

localmin = 0
for v in 'ABC':
    if v in vitamins:
        localmin += vitamins[v]
    else:
        flag = 1
if not flag:
    minPrice = min(localmin, minPrice)


if 'ABC' in vitamins:
    flag = 0
    minPrice = min(vitamins['ABC'], minPrice)

for v in 'ABC':
    vv = 'ABC'.replace(v, '')
    if v in vitamins and vv in vitamins:
        minPrice = min(minPrice, vitamins[vv] + vitamins[v])
        flag = 0


vit = ['AB', 'BC', 'AC']

for v in range(len(vit)):
    for vv in range(v + 1, len(vit)):
        if vit[v] in vitamins and vit[vv] in vitamins:
            flag = 0
            minPrice = min(vitamins[vit[v]] + vitamins[vit[vv]], minPrice)


if flag:
    print(-1)
else:
    print(minPrice)
