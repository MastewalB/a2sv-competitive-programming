def score(cards):
    sereja, dima = 0, 0
    l, r = 0, len(cards) - 1
    turn = 1
    while l <= r:
        if turn:
            sereja += max(cards[l], cards[r])
            turn = 0
        else:
            dima += max(cards[l], cards[r])
            turn = 1

        if cards[l] > cards[r]:
            l += 1
        else:
            r -= 1
    print(sereja, dima)


n = int(input())
cards = list(map(int, input().split()))
score(cards)
