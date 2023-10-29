import sys
input = sys.stdin.readline

def inp():
    return(int(input()))

def lovely_palindrome(n):
    res = str(n)
    res += res[::-1]
##    while n > 0:
##        res += str(n % 10)
##        n //= 10
    return res 

def main():
    n = inp()
    output = lovely_palindrome(n)
    print(output)


if __name__ == "__main__":
    main()
