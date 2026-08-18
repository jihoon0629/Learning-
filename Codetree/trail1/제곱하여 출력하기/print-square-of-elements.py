n=int(input())
arr=list(map(int,input().split()))
new_arr = [arr[i]**2 for i in range(n)]
for i in range(n):
    print(new_arr[i],end=' ')