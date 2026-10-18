n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
arr = []
dis = 0
for i in range(n):
    arr.append(B[i] - A[i])

for i in range(n):
    if arr[i] < 0:
        for j in range(i+1,n):
            if j>0:
                arr[j] = arr[j] + arr[i]
                dis += (j-i) * -arr[i]
                arr[i] = 0
print(dis)