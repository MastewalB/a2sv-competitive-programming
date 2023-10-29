"""

1 2 4 6

1 5 5 7 9


"""


def max_pairs(boys, girls):
    boys.sort()
    girls.sort()
    i = j = pairs = 0

    while i < len(boys) and j < len(girls):
        if abs(boys[i] - girls[j]) <= 1:
            pairs += 1
            i += 1
            j += 1
        elif boys[i] < girls[j]:
            i += 1
        else:
            j += 1

    return pairs


n = int(input())
boys = list(map(int, input().split()))
m = int(input())
girls = list(map(int, input().split()))
print(max_pairs(boys, girls))
