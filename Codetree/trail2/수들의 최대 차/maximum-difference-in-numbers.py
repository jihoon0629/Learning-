N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
max_cnt = 0
for i in range(10001-K):
    cnt = 0
    for j in range(len(arr)):
        if arr[j] >=i and arr[j] <= i+K:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)