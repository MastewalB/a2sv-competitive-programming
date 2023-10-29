

def news(n, groups):
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        x, y = sorted([x, y], key=lambda x: rank[x])
        parent[x] = y
        rank[y] += rank[x]

    parent = [i for i in range(n + 1)]
    rank = [1 for i in range(n + 1)]
    Ans = []

    for g in groups:
        for i in range(1, len(g) - 1):
            union(g[i], g[i + 1])

    for i in range(1, n + 1):
        find(i)

    for i in range(1, n + 1):
        Ans.append(rank[find(i)])

    return Ans


n, m = list(map(int, input().split()))
groups = []
for _ in range(m):
    g = input().split()
    g = [int(num) for num in g]
    groups.append(g)
print(*news(n, groups))


# class UnionFind:
#     def __init__(self, n):
#         self.size = [1] * (n+1)
#         self.parent = [i for i in range(n+1)]

#     def find(self, x):
#         if self.parent[x] == x:
#             return x
#         self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x, y):
#         parent_x = self.find(x)
#         parent_y = self.find(y)
#         if parent_x != parent_y:
#             if self.size[parent_x] >= self.size[parent_y]:
#                 self.parent[parent_y] = parent_x
#                 self.size[parent_x] += self.size[parent_y]
#             else:
#                 self.parent[parent_x] = parent_y
#                 self.size[parent_y] += self.size[parent_x]


# def main():
#     n, m = input().split()
#     n, m = int(n), int(m)
#     unionFind = UnionFind(n)
#     for i in range(m):
#         nums = input().split()
#         nums = [int(num) for num in nums]
#         for j in range(1, len(nums)-1):
#             unionFind.union(nums[j], nums[j+1])

#     for i in range(1, n+1):
#         unionFind.find(i)

#     res = []
#     for i in range(1, n+1):
#         parent_i = unionFind.find(i)
#         res.append(unionFind.size[parent_i])

#     return res


# print(*main())
