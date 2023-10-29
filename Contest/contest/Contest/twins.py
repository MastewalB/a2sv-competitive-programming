def split(coins):
    co = 0
    total = sum(coins)
    half = total / 2
    coins = sorted(coins, reverse=True)

    i = 0
    while i < len(coins) and co < half:
        co += coins[i]
        half -= coins[i]
        i += 1

    print(i) if co > half else print(len(coins))


n = int(input())
coins = list(map(int, input().split()))
split(coins)