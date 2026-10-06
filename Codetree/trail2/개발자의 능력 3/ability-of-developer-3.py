import sys
arr = list(map(int, input().split()))
min_diff = sys.maxsize
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            diff = abs(sum(arr) - 2*(arr[i] + arr[j] + arr[k]))
            min_diff = min(min_diff, diff)
print(min_diff)