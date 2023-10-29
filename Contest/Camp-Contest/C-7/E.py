

def choose(players):
    if len(players) < 2:
        return max(players[0][0], players[1][0])

    for i in range(len(players[0]) - 2, -1, -1):
        players[0][i] = max(players[0][i + 1], players[0]
                            [i] + players[1][i + 1])
        players[1][i] = max(players[1][i + 1], players[1]
                            [i] + players[0][i + 1])

    return max(players[0][0], players[1][0])


def main():
    n = int(input())
    r = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(choose([r, c]))


main()
