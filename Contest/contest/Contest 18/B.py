n, m = list(map(int, input().split()))
poland, enemy = set(), set()
for _ in range(n):
    poland.add(input())
for _ in range(m):
    enemy.add(input())


common = poland.intersection(enemy)
poland = poland.difference(common)
enemy = enemy.difference(common)

even = (len(common) % 2) == 0

if (even and len(poland) > len(enemy)) or (not even and len(poland) > len(enemy)) or (len(common) == 1 and len(poland) >= len(enemy)):
    print("YES")
else:
    print("NO")
