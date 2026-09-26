def f(a,b):
    for i in range(a,a+8):
        for j in range(b,b+8):
            arr[i][j] = 1
    return arr

arr = [[0 for _ in range (201)] for _ in range(201)]
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    f(a+100,b+100)
cnt = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] == 1:
            cnt+=1
print(cnt)