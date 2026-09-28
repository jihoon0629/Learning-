def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

n,t = map(int,input().split())
r,c,d = input().split()
r,c = int(r),int(c)
arr = [r-1,c-1]
dx,dy = [1,0,-1,0], [0,-1,0,1]
direction = {'U':2,'D':0,'R':3,'L':1}
dir = direction[d]
for i in range(t):
    nx,ny = arr[0]+dx[dir],arr[1]+dy[dir]
    if in_range(nx,ny):
        arr[0],arr[1] = nx,ny
    else:
        dir = (dir+2)%4
print(arr[0]+1,arr[1]+1)