from collections import defaultdict, deque


def main():

    n, m = list(map(int, input().split()))
    catCount = list(map(int, input().split()))
    tree = defaultdict(list)
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        tree[a].append(b)
        tree[b].append(a)

    def pathCount(tree, catCount, m):
        visited = set([1])
        queue = deque([(1, catCount[1 - 1])])
        restaurantCount = 0
        while queue:

            for _ in range(len(queue)):
                node, cats = queue.popleft()
                # print(node, cats, queue)
                if cats <= m:
                    neighborCount = 0
                    for neighbor in tree[node]:
                        if neighbor not in visited:
                            neighborCount += 1
                            visited.add(neighbor)
                            if catCount[neighbor - 1]:
                                queue.append(
                                    (neighbor, cats + catCount[neighbor - 1]))
                            else:
                                queue.append((neighbor, 0))
                    if neighborCount == 0:
                        restaurantCount += 1

        return restaurantCount

    print(pathCount(tree, catCount, m))


main()
