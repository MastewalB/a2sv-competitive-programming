def car_fleet(target, position, speed):
    time_stack = []
    time = []
    cars = list(map(lambda psn, spd: (psn, spd), position, speed))
    cars.sort()

    for car in cars:
        time.append((target - car[0]) / car[1])  # s / v = t

    for t in time:
        while time_stack and time_stack[-1] <= t:
            time_stack.pop()
        time_stack.append(t)

    return len(time_stack)
