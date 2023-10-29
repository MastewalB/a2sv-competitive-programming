from collections import Counter

def chat(name):
    count = Counter(name)
    if len(count.keys()) % 2 != 0:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")



name = input().strip()
chat(name)