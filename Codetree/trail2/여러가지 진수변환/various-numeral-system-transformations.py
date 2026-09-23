n,b = map(int,input().split())
arr = []
while True:
    if n<b:
        arr.append(n)
        break
    arr.append(n%b)
    n//=b
arr = arr[::-1]
for i in arr:
    print(i,end='')