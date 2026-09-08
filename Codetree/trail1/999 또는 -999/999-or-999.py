arr=list(map(int,input().split()))
for i in range(len(arr)):
    if arr[i]==999 or arr[i]==-999:
        cnt=i
        break
arr2 = arr[:cnt]
print(max(arr2),min(arr2))