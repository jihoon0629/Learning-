def f(a,b,c,d,n):
    for i in range(a,c):
        for j in range(b,d):  
            arr[i][j] = n
    return arr

arr = [[0 for _ in range(2001)] for _ in range(2001)]
for i in range(1,-1,-1):
    a,b,c,d = map(int,input().split())
    f(a+1000,b+1000,c+1000,d+1000,i)
max_x = 0
max_y = 0
min_x = 2000
min_y = 2000
exist = False
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            exist = True
            if i > max_x:
                max_x = i
            if i < min_x:
                min_x = i
            if j > max_y:
                max_y = j
            if j < min_y:
                min_y = j
if not exist:
    print(0)
else:
    print((max_x - min_x + 1) * (max_y - min_y + 1))