class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        N = len(arr)
        graph = defaultdict(list)
        visited = set([0])
        queue = deque([0])      
        level = 0
        
        
        for i in range(N):
            graph[arr[i]].append(i)
        
        
        while queue:
            size = len(queue)
            for _ in range(size):
                
                curr = queue.popleft()
                if curr == N - 1:
                    return level
                
                neighbours = [curr - 1, curr + 1]
                neighbours.extend(graph[arr[curr]])
                for neighbour in neighbours:
                    if 0 <= neighbour < N and neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
                graph[arr[curr]] = []
            level += 1
        
        