class UnionFind:

    def __init__(self, size):
        self.root = [0]*size
        for i in range(size):
            self.root[i] = (i, 1.0)

    def find(self, x):
        p, xr = self.root[x]
        if x!=p:
            r, pr = self.find(p)
            self.root[x] = (r, pr*xr)
        return self.root[x]

    def union(self, x, y, ratio):
        px, xr= self.find(x)
        py, yr = self.find(y)
        if not ratio:
            return xr / yr if px==py else -1.0
        if px!=py:
            self.root[px] = (py, yr/xr*ratio)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variables = {}
        count = 0
        for a, b in equations:
            if a not in variables:
                variables[a]=count
                count+=1
            if b not in variables:
                variables[b]=count
                count+=1
        n = len(variables)
        uf = UnionFind(n)

        for (a, b), v in zip(equations, values):
            uf.union(variables[a], variables[b], v)

        return [uf.union(variables[a], variables[b], 0) \
                if (a in variables) and (b in variables) else -1 \
                for a, b in queries ]