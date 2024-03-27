for _ in range(int(input())):
    n = int(input())
    result = []
    s = []
    *a, = map(int, input().split())
    i = 0
    while i < n:
        
        if len(s) == 0:
            _min = 1
        elif len(s) == 1:
            _min = s[-1]
        else:
            _min = min(_min, s[-1])
 
        if _min >= len(s) + 1 \
                and a[i] >= len(s) + 1:
            s.append(a[i])
            i += 1
        else:
            result.append(len(s))
            s = []
 
    result.append(len(s))
    print(len(result))
    print(*result)