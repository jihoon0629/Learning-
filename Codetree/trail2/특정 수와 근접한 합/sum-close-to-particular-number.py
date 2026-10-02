import sys
n,s = map(int, input().split())
arr = list(map(int, input().split()))
min_sum = sys.maxsize
for i in range(n):
    for j in range(i+1,n):
        k = arr[:]
        k.pop(i)
        k.pop(j-1)
        min_sum = min(min_sum, abs(sum(k)-s))
print(min_sum)