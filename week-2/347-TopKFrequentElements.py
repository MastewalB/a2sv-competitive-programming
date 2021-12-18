from collections import Counter


def topKFrequent(nums, k):
    response = []
    counted = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)

    for i in range(k):
        response.append(counted[i][0])

    return response


nums = [1, 1, 1, 2, 2, 3]
k = 2
topKFrequent(nums, k)
