import sys
n = int(input())
arr = [int(input()) for _ in range(n)]
min_sum = sys.maxsize
for i in range(n):
    sum = 0
    for j in range(n):
        number = (i + j) % n
        sum += arr[number] * j
    min_sum = min(min_sum, sum)
print(min_sum)