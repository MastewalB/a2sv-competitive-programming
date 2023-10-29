

class SpanningTree:
    def __init__(self, graph):
        self.graph = graph

    def kruskal(self, graph, n):
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        min_span_tree = []
        final_weight = 0

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

        #(source, destination, weight)
        graph = sorted(graph, key=lambda x: x[2])
        for s, d, w in graph:
            if find(s) != find(d):
                min_span_tree.append((s, d, w))
                union(s, d)
                final_weight += w

        for s, d, w in min_span_tree:
            print(f"{s} - {d} - {w}")


graph = [(5, 6, 2), (1, 2, 3), (3, 6, 3), (1, 5, 5),
         (2, 3, 5), (2, 5, 6), (4, 6, 7), (3, 4, 9)]
st = SpanningTree(graph)
st.kruskal(graph, 6)
