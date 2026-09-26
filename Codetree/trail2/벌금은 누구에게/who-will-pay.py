n,m,k = map(int,input().split())
arr = [0 for _ in range(n)]
for i in range(m):
    a = int(input())
    arr[a-1] += 1
    if arr[a-1] == k:
        print(a)
        break
else:
    print(-1)