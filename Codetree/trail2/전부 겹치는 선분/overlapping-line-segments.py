n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)
overlap = False
for i in range(101):
    for x,y in zip(x1,x2):
        if x<=i<=y:
            continue
        else:
            break
    else:
        print('Yes')
        overlap = True
        break
if not overlap:
    print('No')