def operation(a):
    global dir
    if a=='F':
        arr[0]+=dx[dir]
        arr[1]+=dy[dir]
    elif a=='R':
        dir=(dir+1)%4
    else:
        dir=(dir+3)%4
dir = 3
dx, dy = [1,0,-1,0],[0,-1,0,1]
arr = [0,0]
com = input()
time = 0
for i in range(len(com)):
    operation(com[i])
    time += 1
    if arr[0] == 0 and arr[1] == 0:
        print(time)
        break
else:
    print(-1)