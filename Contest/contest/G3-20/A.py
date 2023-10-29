
def isPossible(grid):
    return


t = int(input())
for _ in range(t):
    grid = []
    c = int(input())
    for _ in range(2):
        grid.append(list(map(int, input().split())))
    print(isPossible(grid))
