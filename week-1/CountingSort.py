import random


def countingSort(arr):
    count_arr = [0] * 100
    for i in range(len(arr)):
        count_arr[arr[i]] += 1

    # Place a cursor on the beginning of array
    cursor = 0
    for k in range(len(count_arr)):
        for i in range(count_arr[k]):

            arr[i + cursor] = k
        cursor += count_arr[k]

    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
    return arr


arr = [0, 1, 0, 1, 0]
for i in range(100):
    arr.append(random.randint(0, 99))


countingSort(arr)
