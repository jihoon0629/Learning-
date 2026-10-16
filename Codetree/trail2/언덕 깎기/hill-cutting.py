import sys
N = int(input())
arr = [int(input()) for _ in range(N)]
min_value = sys.maxsize
for i in range(min(arr),max(arr)+1):
    value = 0
    for j in range(len(arr)):
        if arr[j] >= i-9 and arr[j] <= i+8:
            continue
        else:
            if arr[j] > i:
                value += (arr[j] - (i+8))**2
            else:
                value += (arr[j] - (i-9))**2
    min_value = min(min_value, value)
print(min_value)