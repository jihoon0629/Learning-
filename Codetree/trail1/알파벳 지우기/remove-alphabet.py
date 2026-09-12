a = list(input())
arr = []
b = list(input())
arr2 = []
for i in range(len(a)):
    if a[i].isdigit():
        arr.append(a[i])
    else:
        continue

a = ''.join(arr)

for i in range(len(b)):
    if b[i].isdigit():
        arr2.append(b[i])
    else:
        continue
        
b = ''.join(arr2)

print(int(a) + int(b))