a = input()
a1 = a[0]
a2 = a[1]
arr = list(a)
for i in range(len(arr)):
    if arr[i] == a1:
        arr[i] = a2
    elif arr[i] == a2:
        arr[i] = a1
result = ''.join(arr)
print(result)