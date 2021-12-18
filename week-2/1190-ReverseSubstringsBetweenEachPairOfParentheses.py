from collections import deque


def reverse_parentheses(s):
    stack = []
    queue = deque()
    reverse = ""

    for i in s:
        if i != ")":
            stack.append(i)

        if i == ")":
            while stack and stack[-1] != "(":
                queue.append(stack.pop())
            stack.pop()
        while queue:
            stack.append(queue.popleft())
    return "".join(stack)


s = "(u(love)i)"
print(reverse_parentheses(s))
