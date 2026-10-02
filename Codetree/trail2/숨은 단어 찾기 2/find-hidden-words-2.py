def can_move(x,y):
    return x>=0 and x<n and y>=0 and y<m

n,m = map(int, input().split())
arr = [input() for _ in range(n)]
dx,dy = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            for direction in range(8):
                for k in range(1,3):
                    if not can_move(i+dx[direction]*k,j+dy[direction]*k) or arr[i+dx[direction]*k][j+dy[direction]*k] != 'E':
                        break
                else:
                    cnt+=1
print(cnt)