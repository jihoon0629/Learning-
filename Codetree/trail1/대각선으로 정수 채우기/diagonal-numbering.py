n, m = map(int, input().split())

# Please write your code here.
arr=[[0 for _ in range(m)] for _ in range(n)]
num=1
count=0
for k in range(n+m):
    for i in range(n):
        for j in range(m):
            if i+j==count:
                arr[i][j]=num
                num+=1
    count+=1
for i in range(n):
    for j in range(m):
        print(arr[i][j],end=' ')
    print()