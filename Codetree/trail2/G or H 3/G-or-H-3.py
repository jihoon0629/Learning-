n,k = map(int,input().split())
arr = [0 for _ in range(10001)]
for i in range(n):
    a,b = input().split()
    if b=='G':
        arr[int(a)] = 1
    elif b=='H':
        arr[int(a)] = 2

max_sum = 0
for i in range(10001-k):
    sum = 0
    for j in range(k+1):
        sum += arr[i+j]
    max_sum = max(max_sum, sum)
print(max_sum)