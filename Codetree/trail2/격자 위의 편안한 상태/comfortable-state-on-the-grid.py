def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n
n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
dx,dy = [0,1,0,-1],[1,0,-1,0]
for i in range(m):
    x,y = map(int,input().split())
    x-=1
    y-=1
    arr[x][y]=1
    cnt=0
    for nx,ny in zip(dx,dy):
        if in_range(x+nx,y+ny) and arr[x+nx][y+ny]==1:
            cnt+=1
    if cnt==3:
        print(1)
    else:
        print(0)