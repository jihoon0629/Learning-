count=0
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    if arr[i] == 2:
        count+=1
    if count==3:
        print(i+1)
        break