
def rightQueue(queue, front, back):
    begin = None
    second = None
    ans = []
    for a, b in queue:
        if a not in back:
            begin = a
        if a == 0:
            second = b

    while second != 0:
        ans.append(begin)
        ans.append(second)
        begin = front[begin]
        second = front[second] if second in front else 0
    if begin != 0:
        ans.append(begin)
    return ans


def main():
    n = int(input())
    queue = []
    front = {}
    back = set()
    for _ in range(n):
        a, b = list(map(int, input().split()))
        front[a] = b
        back.add(b)
        queue.append([a, b])
    print(*rightQueue(queue, front, back))


main()
