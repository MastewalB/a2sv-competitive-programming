def buildCost(string):
    array = [0 for _ in range(len(string))]
    for i in range(len(string)):
        array[i] = ord(string[i]) - ord('a') + 1

    return array


def cheap(word, p):
    wordArray = buildCost(word)
    total = sum(wordArray)

    return


t = int(input())

for _ in range(t):
    w = input()
    p = int(input())
    print(cheap(w, p))
