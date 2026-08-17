n=int(input())
for i in range(n):
    sum=1
    a,b=map(int,input().split())
    for j in range(a,b+1):
        sum*=j
    print(sum)