def countingSort(arr):
    lst = [0] * 100
    for i in range(len(arr)):
        lst[arr[i]] += 1
    return lst


arr = [0, 1, 0, 0]
print(countingSort(arr))
