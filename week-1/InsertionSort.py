"Given a sorted list with an unsorted number e in the rightmost cell, this code will put e in the right position"


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")


def insertion_sort(n, arr):
    if len(arr) == 1:
        print_arr(arr)
        print()
        return
    current_element = arr[n - 1]
    i = n - 2
    while arr[i] > current_element and i >= 0:

        arr[i + 1] = arr[i]
        print_arr(arr)
        print()

        i -= 1

    arr[i + 1] = current_element
    print_arr(arr)
    print()


arr = [1, 2, 4, 5, 3]
arr = [2, 4, 6, 8, 3]
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
insertion_sort(10, arr)
