import heapq


def toInt(time):
    h, m = time.split(":")
    return (int(h) * 60) + int(m)


def fromInt(time):
    h, m = time // 60, time % 60
    return str(h).zfill(2) + ":" + str(m).zfill(2)


def solution(schedule, time):
    n = len(schedule)

    i = 0
    time = toInt(time)
    while i < n:
        if toInt(schedule[i]) >= time:
            break
        i += 1

    if i < n:
        return fromInt(toInt(schedule[i]) - time)
    return str(-1)


# schedule = ["12:30", "14:00", "19:55"]
# time = "14:00"
# print(solution(schedule, time))


def solution2(numbers, separation):

    n = len(numbers)

    suffix_min = [0] * n
    suffix_min[n - 1] = numbers[n - 1]

    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(suffix_min[i + 1], numbers[i])

    min_sum = float("inf")

    for i in range(n):
        if (i + separation < n):

            min_sum = min(min_sum, abs(numbers[i] -
                          suffix_min[i + separation]))

    return min_sum




numbers = [1, 5, 4, 10, 9]
# numbers = [3, 10, 5, 8]
separation = 3
print(solution3(numbers, separation))
