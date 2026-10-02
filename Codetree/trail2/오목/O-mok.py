def can_move(x,y):
    return x>=0 and x<19 and y>=0 and y<19

arr = [list(map(int,input().split())) for _ in range(19)]
dx,dy = [0,1,1,1],[1,1,0,-1]
find = False
for i in range(19):
    for j in range(19):
        if arr[i][j] != 0:
            color = arr[i][j]
            for direction in range(4):
                for k in range(1,5):
                    if not can_move(i+dx[direction]*k,j+dy[direction]*k) or arr[i+dx[direction]*k][j+dy[direction]*k] != color:
                        break
                else:
                    print(color)
                    print(i+dx[direction]*2+1,j+dy[direction]*2+1)
                    find = True
if not find:
    print(0)