def out_of_range(x,y):
    return x>=0 and x<n and y>=0 and y<m and arr[x][y] == 0

def move(x,y):
    global direction
    nx,ny = x+dx[direction],y+dy[direction]
    if out_of_range(nx,ny):
        jp[0],jp[1] = nx,ny
    else:
        direction = (direction+1)%4
        jp[0],jp[1] = x+dx[direction],y+dy[direction]

n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
alphabet = ord('A')
direction = 0
dx,dy = [0,1,0,-1],[1,0,-1,0]
jp = [0,0]

arr[0][0] = 'A'
for i in range(n*m-1):
    if chr(alphabet) == 'Z':
        alphabet = ord('A')
    else:
        alphabet += 1
    move(jp[0],jp[1])
    arr[jp[0]][jp[1]] = chr(alphabet)

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()