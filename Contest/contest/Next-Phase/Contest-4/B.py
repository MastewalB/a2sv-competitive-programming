def moveBrackets(brackets):
    stack = []

    for bracket in brackets:
        if bracket == "(":
            stack.append(bracket)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(bracket)

    return len(stack) // 2


t = int(input())
for _ in range(t):
    n = int(input())
    brackets = input()
    print(moveBrackets(brackets))
