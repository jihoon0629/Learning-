import sys
n = int(input())
arr = list(map(int,input()))
max_min_vacant = 0
for i in range(n):
    if arr[i] == 0:
        arr2 = arr[:]
        arr2[i] = 1
        min_vacant = sys.maxsize
        vacant = 99999
        for j in range(arr2.index(1),n):
            if arr2[j] == 1:
                vacant += 1
                min_vacant = min(min_vacant, vacant)
                vacant = 0
            else:
                vacant += 1
        max_min_vacant = max(max_min_vacant, min_vacant)
print(max_min_vacant)