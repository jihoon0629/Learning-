n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]
max_area = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j and j!=k and i!=k:
                if x[j] == x[k] and y[j] == y[i]:
                    area = abs(x[j]-x[i]) * abs(y[j]-y[k])
                    max_area = max(max_area, area)
print(max_area)