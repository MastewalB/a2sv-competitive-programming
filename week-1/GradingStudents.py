
def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            continue
        if (5 - (grades[i] % 5)) >= 3:
            continue
        else:
            grades[i] += (5 - (grades[i] % 5))
    return grades


grades = [73, 67, 38, 33]
print(gradingStudents(grades))
