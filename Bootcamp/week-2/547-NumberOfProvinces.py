class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(city):
            visited.add(city)
            for i in range(len(isConnected[city])):
                if (i != city) and (i not in visited) and (isConnected[city][i] == 1):
                    dfs(i)
        provinces = 0
        for i in range(n):
            if not i in visited:
                provinces += 1
                dfs(i)
        return provinces
