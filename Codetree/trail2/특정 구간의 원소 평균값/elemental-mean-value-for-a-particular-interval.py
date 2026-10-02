n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i,n):
        sum = 0
        for k in range(i,j+1):
            sum += arr[k]
        if sum%(j-i+1) == 0:
            av = sum//(j-i+1)
            if av in arr[i:j+1]:
                cnt+=1
print(cnt)