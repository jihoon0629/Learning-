n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)
max_cnt = 0
for i in range(3):
    cnt = 0
    arr = [0,0,0]
    arr[i] = 1
    for j in range(n):
        arr[a[j]-1], arr[b[j]-1] = arr[b[j]-1], arr[a[j]-1]
        if arr[c[j]-1] == 1:
            cnt+=1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)