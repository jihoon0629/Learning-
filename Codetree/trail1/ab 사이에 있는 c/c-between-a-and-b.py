s=False
a,b,c=map(int,input().split())
for i in range(a,b+1):
    if i%c==0:
        s=True
if s:
    print('YES')
else:
    print('NO')