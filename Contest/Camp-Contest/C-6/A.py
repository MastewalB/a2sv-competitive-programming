
def maxDollar(pylons, N):
    dollars = pylons[0]
    energy = 0

    for i in range(1, N):
        if pylons[i] > pylons[i - 1] + energy:
            dollars += pylons[i] - (pylons[i - 1] + energy)
            energy = 0
        else:
            energy += pylons[i - 1] - pylons[i]
    return dollars


n = int(input())
pylons = list(map(int, input().split()))
print(maxDollar(pylons, n))
