import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def main(difficulty, students):
    students.sort()
    left, right = 0, len(students) - 1
    while left <= right:
        mid = left + right >> 1

        if students[mid] >= difficulty:
            right = mid - 1
        else:
            left = mid + 1

    print("Yes") if len(students) // 2 <= left + \
        1 <= (len(students) // 2 + len(students) // 4) else print("No")


if __name__ == "__main__":
    n, m = inlt()
    students = inlt()
    for _ in range(n):
        main(inp(), students)
