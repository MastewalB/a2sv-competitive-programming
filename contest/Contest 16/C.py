#C - Dima and Staircase

def boxHeight(stairs, boxes, n, m):
    maxUpdate = 0
    for box in boxes:
        height = max(maxUpdate, stairs[box[0] - 1])
        print(height)
        maxUpdate = max(maxUpdate, height + box[1])


n = int(input())
stairs = list(map(int, input().split()))
boxes = []
m = int(input())
for _ in range(m):
    boxes.append(list(map(int, input().split())))
boxHeight(stairs, boxes, n, m)
