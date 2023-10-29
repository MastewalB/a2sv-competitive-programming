n = int(input())
p = input()

alphabet = [False] * 26
for letter in p:
    alphabet[ord(letter.lower()) - ord('a')] = True

isPangram = True
for a in alphabet:
    if not a:
        isPangram = False

print("YES") if isPangram else print("NO")
