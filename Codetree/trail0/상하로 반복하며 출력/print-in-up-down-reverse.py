n = int(input())

a = [list(0 for _ in range(n)) for _ in range(n)]

for i in range(n):
    cnt=1
    if i % 2 == 0:
        for j in range(n):
           a[j][i] = cnt
           cnt+=1 
    else:
        for j in range(n-1,-1,-1):
            a[j][i] = cnt
            cnt+=1

for i in range(n):
    for j in range(n):
        print(a[i][j],end='')
    print()