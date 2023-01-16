class SummaryRanges:

    def __init__(self):
        self.parent = {}
    
    def addNum(self, val: int) -> None:
        self.parent[val] = val 
        if val - 1 in self.parent:
            self.union(val, val - 1)
        if val + 1 in self.parent:
            self.union(val, val + 1)

    def getIntervals(self) -> List[List[int]]:
        for key in self.parent.keys():
            self.find(key)
        
        A = {}
        for k in sorted(self.parent.keys()):
            v = self.parent[k]
            if k == v:
                A[k] = v 
            else:
                A[v] = max(A.get(v, v), k)

        return [[s, e] for s, e in A.items()]
    
    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
            
        return self.parent[u]
    
    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        u, v = sorted([u, v])
        self.parent[v] = u

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()