from collections import Counter

n = int(input())
stewards = list(map(int, input().split()))
count = Counter(stewards)
res = len(stewards) - count[min(stewards)] - count[max(stewards)]
print(res) if res >= 0 else print(0)
