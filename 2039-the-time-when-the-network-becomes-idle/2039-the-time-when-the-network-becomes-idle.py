class Solution:
    def buildGraph(self, edges):
        graph = collections.defaultdict(list)
        
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        return graph
    
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = self.buildGraph(edges)
        queue = collections.deque([0])
        serverReachTime = [0] * len(patience)
        visited = set([0])
        
        level = 0
        while queue:
            
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                serverReachTime[node] = level
                for neigh in graph[node]:
                    if neigh not in visited:
                        queue.append(neigh)
                        visited.add(neigh)
                
            level += 1
        
        longest = float("-inf")
        for i in range(1, len(serverReachTime)):
            wait = 2 * serverReachTime[i]
            lastSent = wait % patience[i]
            if patience[i] >= wait:
                lastSent = 0
            else:
                lastSent = wait - lastSent if lastSent else wait - patience[i]
            
            longest = max(longest, lastSent + wait)
        
        return longest + 1