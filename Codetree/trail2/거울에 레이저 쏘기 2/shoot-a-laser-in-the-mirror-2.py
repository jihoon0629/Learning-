def out_of_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

def move(x,y):
    nx,ny = dx[direction],dy[direction]
    if out_of_range(x+nx,y+ny):
        jp[0],jp[1] = x+nx,y+ny
        return 1
    else:
        print(cnt)
        return 0
            

def rotate(x,y):
    global direction
    global cnt
    if arr[x][y]=='/':
        direction = 3-direction
    elif arr[x][y] == '\\':
        if direction in [0,2]:
            direction+=1
        else:
            direction-=1
    cnt+=1

n = int(input())
arr = [input() for _ in range(n)]
jp = []
k = int(input())
dx,dy = [0,1,0,-1],[1,0,-1,0]
cnt = 0
end = True

if k<=n:
    jp.append(0)
    jp.append(k-1)
    direction = 1
elif k<=2*n:
    jp.append(k-n-1)
    jp.append(n-1)
    direction = 2
elif k<=3*n:
    jp.append(n-1)
    jp.append(3*n-k)
    direction = 3
else:
    jp.append(4*n-k)
    jp.append(0)
    direction = 0

while True:
    rotate(jp[0],jp[1])
    if not move(jp[0],jp[1]):
        break