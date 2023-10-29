
def interesting_drink(n, shops, coins):
    shops.sort()
    for i in range(len(coins)):
        left = 0
        right = len(shops) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if coins[i] >= shops[mid]:
                left = mid + 1
            else:
                right = mid - 1
        print(left)


n = int(input())
shops = list(map(int, input().split()))
days = int(input())
coins = []
for _ in range(days):
    coins.append(int(input()))
interesting_drink(n, shops, coins)
