import typing


def removeKdigits(num: str, k: int) -> str:
    i = 0
    stack = []
    while i < len(num):
        while k > 0 and stack and num[stack[-1]] > num[i]:
            stack.pop()
            k -= 1
        stack.append(i)
        i += 1
    while k > 0:
        stack.pop()
        k -= 1

    answer = ""
    found_non_zero = False
    for j in range(len(stack)):
        if num[stack[j]] == "0" and found_non_zero:
            answer += num[stack[j]]
        if num[stack[j]] != "0":
            answer += num[stack[j]]
            found_non_zero = True

    if len(answer) == 0:
        return "0"
    return answer


num = "22345"
k = 2

print(removeKdigits(num, k))

# 120min
