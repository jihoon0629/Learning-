n = int(input())
arr = list(map(int, input().split()))
arr.sort()
chai = []
for i in range(n):
    chai.append(arr[n+i] - arr[i])
print(min(chai))