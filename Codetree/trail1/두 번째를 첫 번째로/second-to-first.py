s = input()
arr = list(s)
a = arr[1]
b = arr[0]
for i in range(len(arr)):
    if arr[i] == a:
        arr[i] = b
print(''.join(arr))