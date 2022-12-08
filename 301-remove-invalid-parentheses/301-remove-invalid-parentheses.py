class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def check(s):
            count = 0
            for c in s:
                if count < 0:
                    return False
                if c == "(":
                    count += 1 
                elif c == ")":
                    count -= 1
            return count == 0
        
        if check(s):
            return [s]
        queue = deque([s])
        visited = set([s])
        res = set()
        found = False
        
        while queue:
            s = queue.popleft()
            
            if check(s):
                res.add(s)
                found = True
            
            if not found:
                for i in range(len(s)):
                    if s[i] in ["(",")"]:
                        t = s[:i] + s[i + 1:]
                        if t not in visited:
                            visited.add(t)
                            queue.append(t)
        return res