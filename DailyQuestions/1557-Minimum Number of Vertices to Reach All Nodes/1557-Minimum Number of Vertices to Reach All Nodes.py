class Solution1:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graphset = set(list(range(n)))
        for i in range(len(edges)):
            if edges[i][1] in graphset:
                graphset.remove(edges[i][1])

        return list(graphset)


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        parents = list(range(n))
        visited = set()
        graph = defaultdict(list)
        for parent, child in edges:
            graph[parent].append(child)

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if(parent1 != parent2):
                parents[node2] = parent1

        def dfs(node):
            visited.add(node)
            for neigh in graph[node]:
                if neigh == find(neigh):
                    union(node, neigh)
                    if neigh not in visited:
                        dfs(neigh)

        for node in range(n):
            dfs(node)
        ans = []
        for node in range(n):
            if find(node) == node:
                ans.append(node)
        return ans
