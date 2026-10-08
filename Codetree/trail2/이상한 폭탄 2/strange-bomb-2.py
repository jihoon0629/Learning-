n,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
explode = []
exist = False
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        elif arr[i] == arr[j] and (abs(i-j) <= k or abs(i-j) >= n-k):
            explode.append(arr[i])
            exist = True
if exist:
    print(max(explode))
else:
    print(-1)