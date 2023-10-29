def checkSorted(array):
    first = second = 0

    if len(array) == 1:
        print("yes")
        print(first + 1, second + 1)
        return

    i = 1
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            if i == len(array) - 1:
                print("yes")
                print(first + 1, second + 1)
                return
        else:
            break

    j = i
    while j < len(array) and array[j] < array[j - 1]:
        if (i > 1 and array[j] < array[i - 2]):
            print("no")
            return
        j += 1

    if j == len(array):
        print("yes")
        print(i, j)
        return

    k = j

    if array[k] < array[i - 1]:
        print("no")
        return

    while k > 1 and k < len(array):
        if array[k] < array[k - 1]:
            print("no")
            return
        k += 1

    print("yes")
    print(i, j)


n = int(input())
array = list(map(int, input().split(" ")))
checkSorted(array)
