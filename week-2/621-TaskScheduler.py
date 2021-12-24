from collections import Counter
import heapq


def taskScheduler(tasks, n):
    if n == 0:
        return len(tasks)
    least_units_of_times = 0
    frequency_dict = list(map(lambda x: -x, Counter(tasks).values()))
    heapq.heapify(frequency_dict)
    time = 0
    processed = len(tasks)

    while processed > 0:
        op = 0
        task = []

        if len(frequency_dict) == 1:
            least_units_of_times += ((-(frequency_dict[0] - 1) * (n + 1)) - n)
            break
        else:
            i = 0
            op = 0
            while i < (n + 1) and frequency_dict:
                task.append(heapq.heappop(frequency_dict))
                op += 1
                i += 1
                processed -= 1

        while task:
            tsk = task.pop()
            tsk += 1
            if -(tsk) > 0:
                heapq.heappush(frequency_dict, tsk)

        least_units_of_times += (n + 1)
    least_units_of_times -= ((n+1) - op)

    return least_units_of_times


tasks = ["A", "A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2
print(taskScheduler(tasks, n))
