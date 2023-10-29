def isPalindrome(time):
    return time == time[::-1]


def toMin(hour):
    hour, minutes = hour.split(":")
    return (int(hour) * 60) + int(minutes)


def toHour(minutes):
    return f"{minutes // 60}:{minutes% 60}"


t = int(input())
for _ in range(t):
    hour, minutes = input().split()
    print(toHour(int(minutes)))
