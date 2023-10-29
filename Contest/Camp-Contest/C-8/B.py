from collections import defaultdict


def minCapacity(log):
    maxCount = count = 0
    entered = set()
    for i in range(len(log)):
        action, person = log[i].split(" ")
        if action == "+":
            entered.add(person)
        else:
            if person in entered:
                entered.remove(person)
            else:
                maxCount += 1

        maxCount = max(maxCount, len(entered))

    return maxCount


def main():
    n = int(input())
    log = []
    for _ in range(n):
        log.append(input())
    print(minCapacity(log))


main()
