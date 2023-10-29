from collections import defaultdict
import sys

sys.setrecursionlimit(8000)


def buildGraph(arr):
    graph = defaultdict(list)
    for e in range(1, len(arr)):
        if arr[e] != -1:
            graph[arr[e]].append(e)
    return graph


def groups(emp_table):
    visited = set()
    depth = 1
    graph = buildGraph(emp_table)

    def dfs(employee, level):
        nonlocal depth
        level += 1
        depth = max(depth, level)
        visited.add(employee)
        for emp in graph[employee]:
            if emp not in visited:
                dfs(emp, level)

    for e in range(1, len(emp_table)):
        if emp_table[e] == -1:
            dfs(e, 0)

    return depth


n = int(input())
employee_table = [0]
for i in range(n):
    employee_table.append(int(input()))
print(groups(employee_table))
