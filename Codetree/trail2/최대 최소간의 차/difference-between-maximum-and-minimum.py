import sys
n, k = map(int, input().split())
arr = list(map(int, input().split()))
min_cnt = sys.maxsize
for h in range(min(arr)+k//2, max(arr)-(k-k//2)+2):
    cnt = 0
    for i in range(n):
        if h-k//2 <= arr[i] <= h+k-k//2:
            continue
        else:
            if arr[i] > h:
                cnt += arr[i] - (h+(k-k//2))
            else:
                cnt += h-k//2 - arr[i]
    min_cnt = min(min_cnt, cnt)
print(min_cnt)