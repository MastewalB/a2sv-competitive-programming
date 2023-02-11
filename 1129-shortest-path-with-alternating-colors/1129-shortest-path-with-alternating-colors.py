class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def buildGraph():
            graph = [[[], []] for _ in range(n)]
            for s, d in redEdges:
                graph[s][0].append(d)
            for s, d in blueEdges:
                graph[s][1].append(d)
            
            return graph 
        
        graph = buildGraph()
        path = [[float("inf"), float("inf")] for _ in range(n)]
        path[0] = [0, 0]

        def dfs(u, color, distance):
            for v in graph[u][color]:
                if distance + 1 < path[v][color]:
                    path[v][color] = distance + 1
                    dfs(v, 1 - color, path[v][color])

        dfs(0, 0, 0)
        dfs(0, 1, 0)

        for i in range(n):
            path[i] = min(path[i])
            if path[i] == float("inf"):
                path[i] = -1
        return path