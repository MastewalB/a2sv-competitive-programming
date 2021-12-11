"Given a sorted list with an unsorted number e in the rightmost cell, this code will put e in the right position"


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def insertion_sort(n, arr):

    for j in range(1, len(arr)):
        print("Currenty Checking - ", arr[j], " - - - ", end=" ")

        i = j - 1
        if arr[j] >= arr[i]:
            print_arr(arr)
            continue
        else:

            # Go back until we find smaller number or to the beginning
            while i >= 0 and arr[j] < arr[i]:
                i -= 1

            # put the number to temporary variable
            temp = arr[j]
            # shift every element to the right of the array to make room for the number
            for k in range(j, i + 1, -1):
                arr[k] = arr[k - 1]
            arr[i + 1] = temp
        print_arr(arr)

    print("Final - ", end=" ")
    print_arr(arr)
    print()


arrays = [
    [1, 2, 4, 5, 3],
    [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
    [1, 4, 3, 5, 6, 2],
    [0, 10, -1]
]
for array in arrays:
    insertion_sort(len(array), array)
