class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        svar = ''

        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        svar = svar.join(stack)
        stack = []

        for char in t:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return ''.join(stack) == svar
