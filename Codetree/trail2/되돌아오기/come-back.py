def move(dir):
    if dir == 'W':
        arr[0] -= 1
    elif dir == 'S':
        arr[1] -= 1
    elif dir == 'N':
        arr[1] += 1
    else:
        arr[0] += 1

n = int(input())
arr = [0,0]
time = 0
find = False
for i in range(n):
    dir,dis = input().split()
    dis = int(dis)
    for j in range(dis):
        time+=1
        move(dir)
        if arr[0] == 0 and arr[1]==0:
            print(time)
            find = True
            break
    if find:
        break
        
else:
    print(-1)