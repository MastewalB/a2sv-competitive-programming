def find_original(changed):
    changed.sort()
    count = dict()
    original = []

    for i in changed:
        if count.get(i / 2):
            if count[i / 2] == 1:
                del count[i / 2]
            else:
                count[i / 2] -= 1
            original.append(i // 2)
        else:
            if count.get(i):
                count[i] += 1
            else:
                count[i] = 1

    return original if len(original) == len(changed) / 2 else []


changed = [1, 3, 4, 2, 6, 8]
changed = [6, 3, 0, 1]
# changed = [2, 1]
print(find_original(changed))
