# main.py
from point_module import read_points
from distance_module import calculate_distance
from triangle_module import find_max_area_triangle

def main():
    # Читаем координаты из файла
    points = read_points("coordinates.txt")
    
    print("Считанные координаты точек:")
    for point in points:
        print(point)

    point1 = points[0]
    point2 = points[1]

    # Расстояние между двумя точками
    distance = calculate_distance(point1, point2)
    print(f"Расстояние между точками {point1} и {point2}: {distance}")

    max_area_triangle, max_area = find_max_area_triangle(points)
    print(f"Треугольник с максимальной площадью: {max_area_triangle}")
    print(f"Максимальная площадь треугольника: {max_area}")


if __name__ == "__main__":
    main()
