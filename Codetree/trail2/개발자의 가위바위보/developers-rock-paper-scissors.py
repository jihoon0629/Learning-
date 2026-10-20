n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*moves)
a, b = list(a), list(b)
upper = 0
lower = 0
for i in range(n):
    if a[i] == b[i]:
        continue
    else:
        if (a[i] == 1 and b[i] == 3) or a[i] == b[i]+1:
            upper += 1
        else:
            lower += 1
print(max(upper, lower))