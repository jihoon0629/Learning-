n, m = map(int, input().split())
pairs = [list(map(int, input().split())) for _ in range(m)]
arr = []
for i in range(m):
    pairs[i].sort()
pairs.sort(key = lambda x: x)
cnt = 1
for i in range(1,m):
    if pairs[i] == pairs[i-1]:
        cnt+=1
    else:
        arr.append(cnt)
        cnt = 1
arr.append(cnt)
print(max(arr))
