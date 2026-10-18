N = int(input())
pigeon = []
position = []
c_n_t = 0
for _ in range(N):
    p, pos = map(int, input().split())
    pigeon.append(p)
    position.append(pos)

for i in range(min(pigeon), max(pigeon)+1):
    arr = []
    for j in range(N):
        if pigeon[j] == i:
            arr.append(position[j])
    if len(arr) == 0:
        continue
    cnt = arr[0]
    for j in range(1,len(arr)):
        if arr[j] != cnt:
            c_n_t += 1
            cnt = arr[j]
print(c_n_t)