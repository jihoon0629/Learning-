import sys
cnt = 0
zero = 0
n, m = map(int, input().split())
arr = list(map(int, input().split()))
if 1 not in arr:
    print(0)
    sys.exit()

for i in range(arr.index(1)-1):
    arr.pop(i)

arr2 = arr[::-1]
for i in range(-arr2.index(1),0):
    arr.pop(i)
for i in range(len(arr)):
    if arr[i] == 1:
        cnt += zero//(2*m+1)
        zero = 0
    else:
        zero += 1
        
if len(arr) <= 2*m + 1:
    print(1)
    sys.exit()
else:
    if len(arr)%(2*m+1) > 0:
        print(len(arr)//(2*m+1) + 1-cnt)
    else:
        print(len(arr)//(2*m+1)-cnt)