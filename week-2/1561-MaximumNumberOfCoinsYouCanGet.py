def maxCoins(piles):
    piles.sort()
    me = len(piles) - 2  # Max coins I can get
    bob = 0
    total = 0
    while bob < me:
        total += piles[me]
        me -= 2
        bob += 1
    return total


piles = [1, 2, 3, 4, 3, 3, 1]
piles = [2, 4, 1, 2, 7, 8]
print(maxCoins(piles))
