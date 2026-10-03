n,k = map(int,input().split())
arr = [0 for _ in range(101)]
for i in range(n):
    a,b = map(int,input().split())
    arr[b] += a
max_sum = 0
if k>=50:
    print(sum(arr))
else:
    for i in range(101-2*k):
        sum = 0
        for j in range(2*k+1):
            sum += arr[i+j]
        max_sum = max(max_sum, sum)
    print(max_sum)