#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#


def componentsInGraph(gb):
    # Write your code here
    parent = defaultdict(int)
    rank = defaultdict(int)
    smallest, largest = 0, 0

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            x, y = sorted([x, y], key=lambda x: rank[x])
            parent[x] = y
            rank[y] += rank[x]
            rank[x] = 0

    for x, y in gb:
        if parent[x] == 0:
            parent[x] = x
            rank[x] = 1
        if parent[y] == 0:
            parent[y] = y
            rank[y] = 1

        newRank = union(x, y)

    for rank in rank.values():
        largest = max(rank, largest)
        if rank > 0:
            smallest = min(smallest, rank) if smallest > 1 else rank
    return smallest, largest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
