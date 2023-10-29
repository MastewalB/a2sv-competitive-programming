def prompt(names):
    usernames = dict()
    for name in names:
        if usernames.get(name):
            print(name + str(usernames[name]))
            usernames[name] += 1
        else:
            usernames[name] = 1
            print("OK")

n = int(input())
names = []
for _ in range(n):
    names.append(input())
prompt(names)