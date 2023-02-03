class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        
        stack = []
        for char in path:
            if char == "..":
                if stack: stack.pop()
            elif char != "." and len(char) > 0:
                stack.append(char)
            
                
        return "/" + "/".join(stack)