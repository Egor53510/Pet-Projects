def min_numbers_to_remove(n, arr):
    freq_map = {}
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    result = 0
    for key in freq_map:
        if key - 1 in freq_map and key + 1 in freq_map:
            result = max(result, freq_map[key - 1] + freq_map[key] + freq_map[key + 1])
        elif key - 1 in freq_map:
            result = max(result, freq_map[key - 1] + freq_map[key])
        elif key + 1 in freq_map:
            result = max(result, freq_map[key] + freq_map[key + 1])
        else:
            result = max(result, freq_map[key])

    return n - result


# Пример использования:
n1 = int(input())
arr1 = list(map(int, input().split()))
print(min_numbers_to_remove(n1, arr1) + 1)
