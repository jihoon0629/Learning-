def out_of_range(x,y):
    return x>=0 and x<n and y>=0 and y<n and arr[x][y]==0

def rotate(x,y):
    global direction
    reverse_direction = (direction + 2) % 4
    rotate_direction = (direction + 3) % 4
    rx,ry = jp[0]+dx[reverse_direction],jp[1]+dy[reverse_direction]
    nx,ny = jp[0]+dx[rotate_direction],jp[1]+dy[rotate_direction]
    if (not out_of_range(rx,ry) or arr[rx][ry] != 0) and arr[nx][ny] == 0:
        return True
    else:
        return False


n = int(input())
arr = [[0] * n for _ in range(n)]
direction = 0
dx,dy = [0,1,0,-1],[1,0,-1,0]
jp = [n//2,n//2]

arr[jp[0]][jp[1]] = 1


for i in range(2,n*n+1):
    if rotate(jp[0],jp[1]):
       direction =  (direction + 3) % 4
    if out_of_range(jp[0]+dx[direction],jp[1]+dy[direction]):
        jp[0],jp[1] = jp[0]+dx[direction],jp[1]+dy[direction]
        arr[jp[0]][jp[1]] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=' ')
    print()