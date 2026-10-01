a,b = map(int, input().split())
arr = [list(input().split()) for _ in range(a)]
current = arr[0][0]
cnt = 0
for i in range(1,a-2):
    for j in range(1,b-2):
        if arr[i][j] != current:
            for i2 in range(i+1,a-1):
                for j2 in range(j+1,b-1):
                    if arr[i2][j2] == current:
                        cnt+=1
if arr[-1][-1] == current:
    print(0)
else:
    print(cnt)