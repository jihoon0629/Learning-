def out_of_range(x,y):
    return x>=0 and x<n and y>=0 and y<m and arr[x][y]==0

def move(x,y):
    global direction
    if out_of_range(jp[0]+dx[direction],jp[1]+dy[direction]):
        jp[0],jp[1] = jp[0]+dx[direction],jp[1]+dy[direction]
    else:
        direction = (direction+3)%4
        jp[0],jp[1] = jp[0]+dx[direction],jp[1]+dy[direction]

n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
arr[0][0] = 1
direction = 1
dx,dy = [0,1,0,-1],[1,0,-1,0]
jp = [0,0]


for i in range(2,n*m+1):
    move(jp[0],jp[1])
    arr[jp[0]][jp[1]] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()