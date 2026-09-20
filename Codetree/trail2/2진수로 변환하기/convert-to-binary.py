n = int(input())
arr = []
while True:
    if n<2:
        arr.append(n)
        break
    arr.append(n%2)
    n//=2
arr=arr[::-1]
for i in arr:
    print(i,end='')