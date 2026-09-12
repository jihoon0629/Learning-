a,b = input().split()
arr = []
for i in range(len(a)):
    if a[i].isdigit():
        lastindex = i
    else:
        break
arr.append(a[:lastindex+1])
for i in range(len(b)):
    if b[i].isdigit():
        lastindex = i
    else:
        break
arr.append(b[:lastindex+1])
print(int(arr[0])+int(arr[1]))