A = input()

# Please write your code here.
arr = []
arr2 = []
for i in A:
    arr.append(i)
for i in range(len(arr)):
    if i == 0:
        arr2.append(arr[i])
        cnt=1
    elif arr[i] != arr[i-1]:
        arr2.append(cnt)
        arr2.append(arr[i])
        cnt=1
    elif arr[i] == arr[i-1]:
        cnt+=1
arr2.append(cnt)
count = 0
for i in arr2:
    count += len(str(i))
print(count)
for i in arr2:
    print(i,end='')