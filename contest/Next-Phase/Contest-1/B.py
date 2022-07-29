def min_days(s):
    day = set()
    count = 0
    for c in s:
        if c not in day:
            if len(day) == 3:
                count += 1
                day.clear()

        day.add(c)
    return count + 1 if len(day) else count


t = int(input())
for _ in range(t):
    s = input()
    print(min_days(s))
