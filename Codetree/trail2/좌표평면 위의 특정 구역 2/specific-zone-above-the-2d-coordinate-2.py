import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
min_area = sys.maxsize
for i in range(n):
    arr_x = x[:]
    arr_y = y[:]
    arr_y.pop(i)
    arr_x.pop(i)
    area = (max(arr_x) - min(arr_x)) * (max(arr_y) - min(arr_y))
    min_area = min(min_area, area)
print(min_area)