n = int(input())
arr = {}
b = {}
w = {}
idx = 0
for i in range(n):
    a, d = input().split()
    a = int(a)
    if d == 'L':
        for j in range(idx-a+1,idx+1):
            w[j] = w.get(j, 0) + 1
            b[j] = b.get(j, 0)
            if w[j] >= 2 and b[j] >= 2:
                arr[j] = 'gray'
            else:
                arr[j] = 'white'
        idx = idx - a + 1
    else:
        for j in range(idx,idx+a):
            w[j] = w.get(j, 0)
            b[j] = b.get(j, 0) + 1
            if w[j] >= 2 and b[j] >= 2:
                arr[j] = 'gray'
            else:
                arr[j] = 'black'
        idx = idx + a - 1
g, b, w = 0, 0, 0
for i in arr:
    if arr[i] == 'gray':
        g += 1
    elif arr[i] == 'black':
        b += 1
    else:
        w += 1
print(w, b, g)