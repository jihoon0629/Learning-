X, Y = map(int, input().split())
cnt = 0
for i in range(X,Y+1):
    arr = list(str(i))
    for j in range(len(arr)):
        if arr.count(arr[j]) == 1:
            if arr.count(arr[j]) + arr.count(arr[j-1]) == len(arr):
                cnt+=1

print(cnt)