n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))
n3 = int(input())
s3 = set(map(int, input().split()))

result = []
for x in s1:
    if x in s2 or x in s3:
        result.append(x)
for x in s2:
    if x in s3 and x not in result:
        result.append(x)

result.sort()
print(*result)