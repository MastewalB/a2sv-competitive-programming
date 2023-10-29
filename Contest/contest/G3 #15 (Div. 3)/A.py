
def shorten(word):
    if len(word) <= 10:
        return word
    return word[0] + str(len(word) - 2) + word[-1]


n = int(input())
for i in range(n):
    word = input()
    print(shorten(word))
