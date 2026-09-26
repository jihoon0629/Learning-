def f(a,b,c,d):
    for i in range(201):
        for j in range(201):
            if i>=a and i < c:
                if j >= b and j < d:
                    arr[i][j] = 1
    return arr
n = int(input())
arr = [[0 for _ in range(201)] for _ in range(201)]
for i in range(n):
    a,b,c,d = map(int,input().split())
    arr = f(a+100,b+100,c+100,d+100)
cnt = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] == 1:
            cnt+=1
print(cnt)