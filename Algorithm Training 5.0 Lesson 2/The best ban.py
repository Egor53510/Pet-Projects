def find_weakest_character(n, m, strengths):
    min_strength = float('inf')
    min_i = 0
    min_j = 0
    for i in range(n):
        for j in range(m):
            if strengths[i][j] < min_strength:
                min_strength = strengths[i][j]
                min_i = i
                min_j = j
    return min_i, min_j

n = 2  # количество рас
m = 2  # количество классов
strengths = [
    [1, 2],
    [3, 4]
]

weakest_race, weakest_class = find_weakest_character(n, m, strengths)
print(f"Михаилу следует запретить расу {weakest_race + 1} и класс с минимальной силой ai j, то есть j={weakest_class + 1}")