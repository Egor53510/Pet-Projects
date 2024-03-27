
from itertools import combinations

def distance_squared(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def find_square_points(points):
    squares = []
    for p1, p2 in combinations(points, 2):
        if p1[0] != p2[0] and p1[1] != p2[1]:
            p3 = (p1[0], p2[1])
            p4 = (p2[0], p1[1])
            if p3 in points and p4 in points:
                squares.append([p1, p2, p3, p4])
    
    if len(squares) == 0:
        # Нет точек, образующих стороны квадрата
        return 2

    return 4 - len(set(sum(squares, [])))

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

additional_points = find_square_points(set(points))

print(additional_points)
# Выбираем произвольные дополнительные точки
for _ in range(additional_points):
    print("0 0") # Пример координат добавленной точки