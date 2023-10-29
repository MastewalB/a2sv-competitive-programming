from collections import defaultdict


def cypher(enemy, n, k):
    ans = 0
    count = defaultdict(int)
    j = 0
    for i in range(n):
        count[enemy[i]] += 1
        while count[enemy[i]] == k:
            ans += n - i
            count[enemy[j]] -= 1
            j += 1
    return ans


n, k = list(map(int, input().split()))
enemy = list(map(int, input().split()))
print(cypher(enemy, n, k))
