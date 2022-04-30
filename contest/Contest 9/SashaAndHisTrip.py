
def minTrip(n, v):
    curr = 1
    price = v if v < n else n - 1
    gas = price

    while (curr + gas) < n:
        curr += 1
        price += (curr * 1)

    return price


def main():
    n, v = list(map(int, input().split()))
    print(minTrip(n, v))


if __name__ == "__main__":
    main()
