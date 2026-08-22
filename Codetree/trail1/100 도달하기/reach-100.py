n=int(input())
arr=[1,n]
while True:
    arr.append(arr[len(arr)-1] + arr[len(arr)-2])
    if arr[-1]>=100:
        break
for i in range(len(arr)):
    print(arr[i],end=' ')