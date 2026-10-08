k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]
cnt = 0
for a in range(n):
    for b in range(n):
        if b==a:
            continue
        for l in range(k):
            if arr[l].index(a+1) > arr[l].index(b+1):
                break
        else:
            cnt+=1
print(cnt)