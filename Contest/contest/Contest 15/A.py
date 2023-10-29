positions = input()

prev = positions[0]
count = 0
for p in positions:
    if p == prev:
        count += 1
    else:
        prev = p
        count = 1
    if count == 7:
        print("YES")
        exit()
print("NO")
