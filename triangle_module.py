from distance_module import calculate_distance

def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def find_max_area_triangle(points):
    max_area = 0
    max_area_triangle = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            for k in range(j + 1, len(points)):
                a = calculate_distance(points[i], points[j])
                b = calculate_distance(points[j], points[k])
                c = calculate_distance(points[k], points[i])

                area = calculate_area(a, b, c)

                if area > max_area:
                    max_area = area
                    max_area_triangle = (points[i], points[j], points[k])

    return max_area_triangle, max_area
