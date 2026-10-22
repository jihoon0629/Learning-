import sys

n = int(input())
arr2 = list(map(int, input().split()))
arr = arr2[:]
if len(set(arr)) == 1:
    print(-1)
    sys.exit()
for i in range(arr.count(min(arr))):
    arr.pop(arr.index(min(arr)))
if arr.count(min(arr)) > 1:
    print(-1)
    sys.exit()
else:
    print(arr2.index(min(arr))+1)