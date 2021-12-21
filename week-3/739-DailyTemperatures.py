def daily_temperatures(temperatures):
    output = [0] * len(temperatures)
    stack = []

    stack.append(0)
    for i in range(1, len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            output[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)

    return output
