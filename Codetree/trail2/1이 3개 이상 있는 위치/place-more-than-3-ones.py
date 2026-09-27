n = int(input())
def in_range(x,y):
    global n
    return x>=0 and x<n and y>=0 and y<n
arr = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [1,0,-1,0], [0,-1,0,1]
count = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for nx, ny in zip(dx, dy):
            if in_range(i+nx,j+ny) and arr[i+nx][j+ny] == 1:
                cnt+=1
        if cnt >= 3:
            count += 1
print(count)