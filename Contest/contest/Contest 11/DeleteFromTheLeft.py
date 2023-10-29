def minMoves(s, t):
    i = -1
    minLen = len(s) if len(s) < len(t) else len(t)
    while -i - 1 < minLen and s[i] == t[i]:
        i -= 1

    i = -(i + 1)
    moves = (len(s) - i) + (len(t) - i)
    return moves


if __name__ == "__main__":
    s, t = input(), input()
    print(minMoves(s, t))
