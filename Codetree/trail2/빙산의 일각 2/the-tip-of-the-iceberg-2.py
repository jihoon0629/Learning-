n = int(input())
arr = [int(input()) for _ in range(n)]
max_cnt = 0
for i in range(1000):
    new_arr = arr[:]
    cnt = 0
    for k in range(n):
        new_arr[k] -= i
        if k==0 and new_arr[k] <= 0:
            continue
        elif k == len(arr)-1 and new_arr[k]>0:
            cnt+=1
        else:
            if new_arr[k] <= 0 and new_arr[k-1] > 0:
                cnt+=1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)