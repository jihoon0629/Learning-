n,t = map(int,input().split())
arr = list(map(int,input().split()))
max_cnt = 0
cnt = 0
for i in range(n):
    if arr[i] <= t:
        cnt = 0
    else:
        cnt+=1
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)