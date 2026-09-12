arr = list(input())
arr2=[]
for i in arr:
    if ord(i) >= ord('A') and ord(i) <= ord('Z'):
        arr2.append(i.lower())
    else:
        arr2.append(i.upper())
print(''.join(arr2))