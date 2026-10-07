n,b = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
max_cnt = 0
for i in range(n):
    money = b-arr[i]//2
    cnt = 1
    for j in range(n):
        if j==i:
            continue
        else:
            if money-arr[j]>=0:
                money-=arr[j]
                cnt+=1
            else:
                continue
    max_cnt = max(max_cnt, cnt)
print(max_cnt)