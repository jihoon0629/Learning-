n=int(input())
arr=list(map(int,input().split()))
new_arr = [arr[i] for i in range(n) if arr[i]%2==0]
for i in range(len(new_arr)):
    print(new_arr[i],end=' ')