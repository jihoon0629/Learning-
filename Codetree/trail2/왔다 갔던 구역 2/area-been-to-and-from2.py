n = int(input())
idx = 0
arr = [0 for _ in range(1001)]
for i in range(n):
    a,b = input().split()
    if b == 'R':
        for j in range(int(a)):
            arr[idx] += 1
            idx += 1
    else:
        for j in range(int(a)):
            idx -= 1
            arr[idx] +=1
            
cnt = 0
for i in arr:
    if i >= 2:
        cnt += 1
print(cnt)