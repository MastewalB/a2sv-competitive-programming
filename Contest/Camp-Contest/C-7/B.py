
def inc(stack):
    N = len(stack)
    for i in range(N):

        if i < N - 1:
            diff = 0
            if i > 0:
                if stack[i] > stack[i - 1]:
                    diff = stack[i] - stack[i - 1] - 1
            else:
                diff = stack[i]
            stack[i + 1] += diff
            stack[i] -= diff

    for i in range(N):
        if i > 0 and stack[i] <= stack[i - 1]:
            return "NO"
    return "YES"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        stack = list(map(int, input().split()))
        print(inc(stack))


main()
