from collections import defaultdict

def handle(handles):
    h = defaultdict(str)
    for o, n in handles:
        h[o] = n 

    visited = set()
    output = {}
    
    for old, new in handles:
        if old not in visited:
            key = old
            while h[old]:
                visited.add(old)
                old = h[old]
            output[key] = old
    print(len(output.items()))
    for k, v in output.items():
        print(k, v)

n = int(input())
handles = []
for _ in range(n):
    handles.append(input().split())
handle(handles)