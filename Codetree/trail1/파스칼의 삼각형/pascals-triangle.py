n=int(input())
arr=[[1 for _ in range(i+1)] for i in range(n)]
for i in range(n):
    for j in range(i+1):
        if j==0 or j==i:
            continue
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
for i in range(n):
    for j in range(i+1):
        print(arr[i][j],end=' ')
    print()