import sys
n = int(input())
arr = list(map(int, input().split()))
now = 1000000000
cnt = 0
for i in range(-1,-n-1,-1):
    if now > arr[i]:
        cnt += 1
        now = arr[i]
    else:
        break
print(n-cnt)