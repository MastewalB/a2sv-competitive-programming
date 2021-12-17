def counting_valleys(steps, path):
    sea_level = 0
    valleys = 0
    mountains = 0

    for i in path:
        if i == "D":
            sea_level -= 1
            if sea_level == 0:
                mountains += 1
        else:
            sea_level += 1
            if sea_level == 0:
                valleys += 1
    return valleys


steps = 12
path = "DDUUDDUDUUUD"
print(counting_valleys(steps, path))
