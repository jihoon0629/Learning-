s,q = input().split()
arr = list(s)
for i in range(int(q)):
    a,b,c = input().split()
    if int(a)==1:
        b = int(b)
        c = int(c)
        temp = arr[b-1]
        arr[b-1] = arr[c-1]
        arr[c-1] = temp

    else:
        for i in range(len(arr)):
            if arr[i] == b:
                arr[i] = c
    print(''.join(arr))