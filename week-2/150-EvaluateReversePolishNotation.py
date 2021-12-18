class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["-", "+", "/", "*"]
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == "*":
                    t = a * b
                elif token == "+":
                    t = a + b
                elif token == "/":
                    t = b / a
                else:
                    t = b - a

                stack.append(str(int(t)))
        return int(stack[0])
