def merge(intervals):
    for i in range(len(intervals)):
        minimum = i
        for j in range(i + 1, len(intervals)):
            if intervals[j][0] < intervals[minimum][0]:
                minimum = j
        intervals[i], intervals[minimum] = intervals[minimum], intervals[i]
        print(intervals)

    print("Sorted ", intervals)
    i = 0
    while (i < len(intervals) - 1):
        if intervals[i][1] >= intervals[i + 1][0]:
            temp = intervals.pop(i + 1)
            if intervals[i][1] <= temp[1]:
                intervals[i][1] = temp[1]

            i -= 1
        i += 1
    return intervals


intervals = [[1, 2], [5, 8], [3, 6], [6, 7]]
intervals = [[4, 5], [2, 4], [4, 6], [3, 4], [0, 0], [1, 1], [3, 5], [2, 2]]
# intervals = [[0, 0], [1, 1], [2, 2], [2, 4], [3, 4], [3, 5], [4, 5], [4, 6]]
print(merge(intervals))
