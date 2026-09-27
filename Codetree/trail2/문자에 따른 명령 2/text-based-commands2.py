def rot(a):
    global direction
    if a=='R':
        direction = (direction+1)%4
    if a=='L':
        direction = (direction+3)%4
    if a=='F':
        arr[0] += dx[direction]
        arr[1] += dy[direction]
direction = 3
dx = [1,0,-1,0]
dy = [0,-1,0,1]
arr = [0, 0]
dirs = input()
for i in range(len(dirs)):
    rot(dirs[i])
print(arr[0],arr[1])