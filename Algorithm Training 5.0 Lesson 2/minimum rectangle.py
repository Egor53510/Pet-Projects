n = int(input())
array = [0] * n
for i in range(n):
    array[i] = [0] * 2
for i in range(n):
    array[i][0] = int(input())
    array[i][1] = int(input())


# Нахождение минимальных и максимальных значений координат
min_x = min(coord[0] for coord in array)
max_x = max(coord[0] for coord in array)
min_y = min(coord[1] for coord in array)
max_y = max(coord[1] for coord in array)

# Запись результата в выходной файл
print(min_x," ", min_y)
print(min_y," ", max_y)