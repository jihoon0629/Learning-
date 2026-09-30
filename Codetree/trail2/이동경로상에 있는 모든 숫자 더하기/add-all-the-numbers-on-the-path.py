def can_move(x,y):
    return x>=0 and x<n and y>=0 and y<n
n,t = map(int,input().split())
com = input()
direction = 3
dx,dy = [0,1,0,-1],[1,0,-1,0]
jp = [n//2,n//2]
arr = [list(map(int,input().split())) for _ in range(n)]

sum = arr[jp[0]][jp[1]]
for i in range(t):
    if com[i] == 'F':
        nx,ny = jp[0]+dx[direction],jp[1]+dy[direction]
        if can_move(nx,ny):
            jp[0],jp[1] = nx,ny
            sum = sum + arr[jp[0]][jp[1]]
        else:
            continue
    elif com[i] == 'L':
        direction = (direction+3)%4
    else:
        direction = (direction+1)%4

print(sum)