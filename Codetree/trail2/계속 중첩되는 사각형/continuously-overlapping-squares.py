def f(a,b,c,d,color):
    for x in range(a+100,c+100):
        for y in range(b+100,d+100):
            arr[x][y] = color
arr = [[None for _ in range(201)] for _ in range(201)]
n = int(input())
for i in range(n):
    a,b,c,d = map(int,input().split())
    if i%2==0:
        f(a,b,c,d,'red')
    else:
        f(a,b,c,d,'blue')
cnt=0
for i in range(201):
    for j in range(201):
        if arr[i][j] == 'blue':
            cnt+=1
print(cnt)