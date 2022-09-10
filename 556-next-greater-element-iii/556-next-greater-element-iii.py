class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        n = list(map(int, str(n)))
        response = []
        stack = []
        
        for i in range(len(n) - 1, -1, -1):
            while stack and stack[-1] > n[i]:
                response.append(stack.pop())
            stack.append(n[i])
            if response:
                response = n[:i] + [response.pop()] + sorted(response + stack)
                response = int(''.join(map(str, response)))
                return response if response < 2147483648 else -1
        
        return -1
            