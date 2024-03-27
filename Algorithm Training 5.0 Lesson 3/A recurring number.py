n, k = map(int, input().split())
numbers = list(map(int, input().split()))

last_seen = {}  # словарь для хранения индексов последнего появления числа
for i in range(n):
    if numbers[i] in last_seen and i - last_seen[numbers[i]] <= k:
        print("YES")
        break
    last_seen[numbers[i]] = i  # обновляем индекс последнего появления числа
else:
    print("NO")