def invalidate(word):
    if len(word) == 1 and word[0] == 'a':
        print("NO")
        return
    word = ['a'] + list(word)
    left, right = 0, len(word) - 1

    while left < right and word[left] == word[right]:
        word[left], word[left + 1] = word[left + 1], word[left]
        left += 1
        right -= 1
    if left > right:
        print("NO")
    elif left == right and word[left - 1] == word[left + 1]:
        print("NO")
    else:
        print("YES")
        print(''.join(word))


t = int(input())
for _ in range(t):
    word = input()
    invalidate(word)
