class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped.reverse()
        i = 0
        while i < len(pushed):
            if pushed[i] != popped[-1]:
                stack.append(pushed[i])
            else:
                popped.pop()
            while stack and popped:
                if popped[-1] == stack[-1]:
                    popped.pop()
                    stack.pop()
                else:
                    break
            i += 1

        return len(stack) == 0
