class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def buildGraph(edges):
            graph = collections.defaultdict(set)
            for x, y in edges:
                graph[x].add(y)
            
            return graph
        
        redGraph = buildGraph(redEdges)
        blueGraph = buildGraph(blueEdges)
        path = [float("inf") for _ in range(n)]
        
        def bfs(initial):
            queue = collections.deque([0])
            visited = set()
            level = 0
            
            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    path[node] = min(path[node], level)
                    if initial:
                        for neigh in redGraph[node]:
                            if (node, neigh, initial) not in visited:
                                visited.add((node, neigh, initial))
                                queue.append(neigh)
                    else:
                        for neigh in blueGraph[node]:
                            if (node, neigh, initial) not in visited:
                                visited.add((node, neigh, initial))
                                queue.append(neigh)
                
                level += 1
                initial = 1 - initial
        
        bfs(0)
        bfs(1)
        
        for i in range(n):
            if path[i] == float("inf"):
                path[i] = -1
        return path