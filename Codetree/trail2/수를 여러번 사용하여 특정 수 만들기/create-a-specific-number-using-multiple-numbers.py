A, B, C = map(int, input().split())
max_pos = 0
for i in range(1000):
    for j in range(1000):
        if A*i + B*j <= C:
            max_pos = max(max_pos, A*i + B*j)
print(max_pos)