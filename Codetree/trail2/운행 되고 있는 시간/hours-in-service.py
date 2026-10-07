n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
a = [t[0] for t in times]
b = [t[1] for t in times]
max_time = 0
for i in range(n):
    arr = [0 for _ in range(1001)]
    time = 0
    for j in range(n):
        if j==i:
            continue
        for k in range(a[j],b[j]):
            arr[k]+=1
    for k in range(len(arr)):
        if arr[k]!=0:
            time+=1
    max_time = max(max_time,time)
print(max_time)