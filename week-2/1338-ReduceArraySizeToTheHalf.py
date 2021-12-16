def min_set_size(arr):
    n = len(arr)
    count = dict()
    new_length = 0
    size = 0

    for i in range(n):
        if count.get(arr[i]):
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1
    sorted_dict = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
    for i in sorted_dict:
        print("new ", new_length)
        if new_length >= n / 2:
            break

        print(i, sorted_dict.get(i))
        new_length += sorted_dict.get(i)
        size += 1

    print(sorted_dict)
    return size


arr = [3, 3, 3, 5, 4, 2, 2, 2, 2, 3, 5, 5, 5, 2, 2, 1]
arr = [7, 7, 7, 7, 7, 7]
arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
ans = min_set_size(arr)
print(ans)
