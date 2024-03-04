def read_points(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
    return points
