n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
overlap = False
for i in range(101):
    for x1,x2 in segments:
        if x1<=i<=x2:
            continue
        else:
            break
    else:
        print('Yes')
        overlap = True
        break
if not overlap:
    print('No')