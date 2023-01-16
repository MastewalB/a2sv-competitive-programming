class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return parent[u]
        
        parent = list(range(len(vals)))
        G = defaultdict(list)
        for u, v in edges:
            G[u].append(v)
            G[v].append(u)
        
        value_count = defaultdict(lambda: defaultdict(int))
        for node, val in enumerate(vals):
            value_count[node][val] = 1
        
        V = sorted([[val, node] for node, val in enumerate(vals)])
        ans = len(vals)

        for val, node in V:
            for neigh in G[node]:
                u, v = find(node), find(neigh)
                if vals[neigh] <= val and u != v:
                    parent[v] = u
                    ans += value_count[u][val] * value_count[v][val]
                    value_count[u][val] += value_count[v][val]
        return ans