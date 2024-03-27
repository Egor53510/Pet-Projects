w=str(input())
e=str(input())
k=1
q='qwertyuiopasdfghjklzxcvbnm'
for i in range(len(q)):
    if w.count(q[i])!=e.count(q[i]):
        k=0
        break
if k==1:
    print('YES')
else:
    print('NO')