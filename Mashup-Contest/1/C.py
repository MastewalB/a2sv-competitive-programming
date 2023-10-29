def minVaried(s):
    if s <= 9:
        return s

    nums = set()
    single = 9
    while s > 0:
        if str(single) not in nums:
            if s >= single:
                nums.add(str(single))
                s -= single
            single -= 1
            if single == 0:
                single = s

    return ''.join(sorted(list(nums)))


t = int(input())
for _ in range(t):
    s = int(input())
    print(minVaried(s))
