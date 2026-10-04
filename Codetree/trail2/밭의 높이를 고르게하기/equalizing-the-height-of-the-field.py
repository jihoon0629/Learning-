import sys
n,h,t = map(int,input().split())
arr = list(map(int,input().split()))
min_sum = sys.maxsize
for i in range(n-t+1):
    sum = 0
    for j in range(t):
        sum += abs(arr[i+j]-h)
    min_sum = min(min_sum, sum)
print(min_sum)