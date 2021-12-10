def select(arr, i):
    min_index = i
    for j in range(i + 1, len(arr)):
        if int(arr[j][-1]) < int(arr[min_index][-1]):
            min_index = j

    return min_index


def sort_sentence(s):
    arr = s.split(" ")
    for i in range(len(arr)):
        min_index = select(arr, i)
        arr[min_index], arr[i] = arr[i], arr[min_index]
    for i in range(len(arr)):
        arr[i] = arr[i][:-1]
    print(arr)


s = "Myself2 Me1 I4 and3"
sort_sentence(s)
