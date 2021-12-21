from collections import defaultdict


def next_greater_element(nums1, nums2):
    dictionary = defaultdict(lambda: -1)
    print(dictionary)
    stack = []
    response = []

    stack.append(nums2[0])
    for i in range(1, len(nums2)):
        while stack and nums2[i] > stack[-1]:
            dictionary[stack[-1]] = nums2[i]
            stack.pop()
        stack.append(nums2[i])

    for j in range(len(nums1)):
        if dictionary.get(nums1[j]):
            response.append(dictionary.get(nums1[j]))
        else:
            response.append(-1)
    return response


nums1 = [1, 3, 5, 2, 4]
nums2 = [6, 5, 4, 3, 2, 1, 7]

next_greater_element(nums1, nums2)
