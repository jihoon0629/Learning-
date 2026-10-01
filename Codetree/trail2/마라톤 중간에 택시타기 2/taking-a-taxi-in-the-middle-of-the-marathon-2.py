import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
min_sum = sys.maxsize

for i in range(1,n-1):    
    sum = 0
    arr_x, arr_y = x[:], y[:]
    arr_x.pop(i)
    arr_y.pop(i)
    for j in range(1,n-1):
        sum += (abs(arr_x[j] - arr_x[j-1]) + abs(arr_y[j] - arr_y[j-1]))
    min_sum = min(min_sum, sum)

print(min_sum)