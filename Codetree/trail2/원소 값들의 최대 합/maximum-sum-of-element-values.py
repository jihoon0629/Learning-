n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
max_amount = 0
for i in range(1,n+1):
    ind = i
    amount = 0
    for j in range(m):
        amount += arr[ind]
        ind = arr[ind]
    max_amount = max(max_amount, amount)
print(max_amount)