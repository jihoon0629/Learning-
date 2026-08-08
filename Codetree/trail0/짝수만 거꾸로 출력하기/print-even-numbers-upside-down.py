n = int(input())
a= list(map(int,input().split()))
a = a[::-1]
for i in range(n):
    if a[i]%2==0:
        print(a[i],end=' ')