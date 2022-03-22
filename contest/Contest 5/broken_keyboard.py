import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))



def broken_keyboard(string):
    response = dict()
    i = 0
    while i < len(string):
        count = 1
        j = i + 1
        while j < len(string) and string[j] == string[i]:
            j += 1
            count += 1
        if count < 2 or count % 2 != 0:
            if not response.get(string[i]):
                response[string[i]] = 1
        i = j

    res = list(response.keys())
    res.sort()
    return ''.join(res)

def main():
    t = inp()
    res = []
    for i in range(t):
        r = broken_keyboard(insr())
        res.append(r)
    for r in res:
        print(r)


if __name__ == "__main__":
    main()
