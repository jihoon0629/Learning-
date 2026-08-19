arr=list(map(int,input().split()))
for i in range(10):
    arr.append((arr[i]+arr[i+1])%10)
    print(arr[i],end=' ')
