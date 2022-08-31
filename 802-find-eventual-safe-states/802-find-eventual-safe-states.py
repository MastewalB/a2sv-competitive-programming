class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def buildGraph(outDeg):
            inDeg = defaultdict(set)
            
            for i in range(len(graph)):
                inDeg[i]
                for b in graph[i]:
                    if b != i:
                        inDeg[b].add(i)
        
            return inDeg
        
        inDeg = buildGraph(graph)
        queue = deque()
        res = []
        
        for i in range(len(graph)):
            graph[i] = set(graph[i])
        for i in range(len(graph)):
            if not graph[i]:
                queue.append(i)
        # print(inDeg)
        # print(graph)
        while queue:
            node = queue.popleft()
            res.append(node)
            for neigh in inDeg[node]:
                # print(neigh)
                graph[neigh].remove(node)
                if len(graph[neigh]) == 0:
                    queue.append(neigh)
        
        res.sort()
        return res
            