def reverse_array(array, index):
    left = 0
    right = index
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

    return array


def pancake_sort(array):
    left = 1
    right = len(array)
    flips = []

    while left < right:
        for i in range(len(array) - 1, -1, -1):
            if array[i] == right:
                reverse_array(array, i)
                flips.append(i + 1)
                reverse_array(array, right - 1)
                flips.append(right)
                right -= 1

    return array


array = [3, 2, 4, 1]
print(pancake_sort(array))
