n = int(input())
arr = {}
idx = 0
for i in range(n):
    a,b = input().split()
    a = int(a)
    if b == 'L':
        for j in range(idx - a + 1, idx + 1):
            arr[j] = 'white'
        idx = idx - a + 1
    else:
        for j in range(idx, idx + a):
            arr[j] = 'black'
        idx = idx + a - 1
b,w = 0,0
for i in arr:
    if arr[i] == 'black':
        b += 1
    if arr[i] == 'white':
        w += 1
print(w,b)