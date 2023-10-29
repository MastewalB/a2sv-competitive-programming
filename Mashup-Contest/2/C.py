from collections import defaultdict


def reconstruct(subs, elem, array):
    response = []
    while subs[elem][1] != subs[elem][2]:
        response.append(subs[elem][2] + 1)
        elem = array[subs[elem][1]]

    if elem:
        response.append(subs[elem][2] + 1)
    response.reverse()
    return response


def reconstructArray(elem, array, length):
    response = []

    for i in range(len(array) - 1, -1, -1):
        if array[i] == elem:
            response.append(i + 1)
            elem -= 1
            length -= 1
        if length == 0:
            break
    response.reverse()
    return response


def consecutive(array, N):
    subs = defaultdict()
    maxLen = 0
    maxElem = None

    for i in range(N):
        if array[i] - 1 in subs:
            subs[array[i]] = (subs[array[i] - 1][0] + 1,
                              subs[array[i] - 1][2], i)
        else:
            subs[array[i]] = (1, i, i)
        if subs[array[i]][0] > maxLen:
            maxLen = subs[array[i]][0]
            maxElem = array[i]

    print(maxLen)
    print(*reconstructArray(maxElem, array, maxLen))


n = int(input())
array = list(map(int, input().split()))
consecutive(array, n)
