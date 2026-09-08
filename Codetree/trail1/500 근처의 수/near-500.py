arr=list(map(int,input().split()))
arr.sort(reverse=False)
for i in range(len(arr)):
    if arr[i]<500 and arr[i+1] > 500:
        print(arr[i],arr[i+1])