class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        
        def buildGraph(conditions):
            inDeg = defaultdict(set)
            outDeg = defaultdict(set)
            
            for a, b in conditions:
                inDeg[b].add(a)
                outDeg[a].add(b)
            return inDeg, outDeg
        
        
        def ts(conditions):
            inDeg, outDeg = buildGraph(conditions)
            tSort = []
            zeroIncoming = []
            for x in range(1, k + 1):
                if x not in inDeg:
                    zeroIncoming.append(x)

            queue = deque(zeroIncoming)
            while queue:
                node = queue.popleft()
                tSort.append(node)
                for neigh in outDeg[node]:
                    inDeg[neigh].remove(node)
                    if len(inDeg[neigh]) == 0:
                        queue.append(neigh)
            
            return tSort
        
        rowTs = ts(rowConditions)
        colTs = ts(colConditions)
        
        if len(rowTs) < k or len(colTs) < k:
            return 
        
        res = [[0 for _ in range(k)] for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if rowTs[i] == colTs[j]:
                    res[i][j] = rowTs[i]
                
        return res