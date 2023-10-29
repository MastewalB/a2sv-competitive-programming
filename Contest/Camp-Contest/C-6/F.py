from collections import defaultdict


def main():
    n, m = list(map(int, input().split()))
    outGoing = defaultdict(int)
    graph = defaultdict(list)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        outGoing[a] += 1
        outGoing[b]

    queue = [[k, v] for k, v in outGoing.items()]
    queue.sort(key=lambda x: [-x[1], x[0]])
    print(queue)
    answer = [0] * n
    curr = 1
    for node, count in queue:
        answer[node - 1] += curr
        for neighbor in graph[node]:
            answer[neighbor - 1] += 1
    print(*answer)


main()
