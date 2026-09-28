def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<m and arr[x][y]==0
n,m = map(int,input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
arr[0][0] = 1
coord = [0,0]
dx,dy = [0,1,0,-1],[1,0,-1,0]
dir = 0
for i in range(2,n*m+1):
    nx,ny = coord[0]+dx[dir],coord[1]+dy[dir]
    if not in_range(nx,ny):
        dir = (dir+1)%4
    coord[0]+=dx[dir]
    coord[1]+=dy[dir]
    arr[coord[0]][coord[1]]=i
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()