n = int(input())
sectors = list(map(int, input().split()))
a, b, k = map(int, input().split())

na = (a-1) // k
nb = (b-1) // k
if(nb - na >= n-1):
    nb = na + n-1

m = -1
for i in range(na, nb+1):
    m = max(m, sectors[i % n], sectors[(n - (n+i)) % n ])
print(m)