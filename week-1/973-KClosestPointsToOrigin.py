import math


def calculate_distance(point_1, point_2):
    d = math.sqrt(((point_1[0] - point_2[0]) ** 2) +
                  ((point_1[1] - point_2[1]) ** 2)
                  )
    return d


def k_closest(points, k):
    origin = [0, 0]
    for i in range(k):

        min_distance = calculate_distance(points[i], origin)
        min_distance_index = i

        for j in range(i + 1, len(points)):
            distance = calculate_distance(points[j], origin)

            if distance < min_distance:

                min_distance = distance
                min_distance_index = j
            points[i], points[min_distance_index] = points[min_distance_index], points[i]
    return points[:k]


points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(k_closest(points, k))
