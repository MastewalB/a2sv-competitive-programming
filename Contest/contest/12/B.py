def form(queue, t):
    queue = list(queue)
    for i in range(t):
        j = 1
        while j < len(queue):
            if(queue[j] == 'G' and queue[j - 1] == 'B'):
                queue[j], queue[j - 1] = queue[j - 1], queue[j]
                j += 2
            else:
                j += 1
    print(''.join(queue))

n, t = list(map(int, input().split()))
queue = input()
form(queue, t)