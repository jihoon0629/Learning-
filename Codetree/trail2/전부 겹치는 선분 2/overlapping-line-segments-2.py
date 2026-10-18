n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
for h in range(n):
    x1 = [i[0] for i in segments]
    x2 = [i[1] for i in segments]
    x1.pop(h)
    x2.pop(h)
    if min(x2) >= max(x1):
        print('Yes')
        break
    else:
        continue
else:
    print('No')