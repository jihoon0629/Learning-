n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr2 = []
for i in range(n):
    if i==0:
        cnt=1
    elif arr[i] != arr[i-1]:
        arr2.append(cnt)
        cnt=1
    elif arr[i] == arr[i-1]:
        cnt+=1
arr2.append(cnt)
print(max(arr2))