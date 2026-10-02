def carry(a,b,c):
    cry = 10
    for i in range(4):
        if (a%cry + b%cry + c%cry) >= cry:
            return False
        cry*=10
    return True

n = int(input())
arr = [int(input()) for _ in range(n)]
max_sum = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if carry(arr[i],arr[j],arr[k]):
                max_sum = max(max_sum, arr[i]+arr[j]+arr[k])
if max_sum == 0:
    print(-1)
else:
    print(max_sum)