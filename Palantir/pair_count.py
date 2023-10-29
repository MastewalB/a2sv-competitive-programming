from collections import Counter


def solution(A, B, queries):
    freq = Counter(A)
    res = []

    def assign(index, val):
        freq[A[index]] -= 1
        A[index] = val
        freq[A[index]] += 1

    def count(target):
        ans = 0
        for a in B:
            ans += freq[target - a]
        return ans

    for q in queries:
        if q[0] == 0:
            assign(q[1], q[2])
        else:
            res.append(count(q[1]))
    return res


A = [3, 4]
B = [1, 2, 3]
queries = [[1, 5], [0, 0, 1], [1, 5]]
print(solution(A, B, queries))
