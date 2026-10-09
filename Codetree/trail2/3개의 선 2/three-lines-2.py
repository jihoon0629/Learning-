n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)
pos = False
for i in range(11):
    for j in range(11):
        for k in range(11):
            for l in range(2):
                for p in range(2):
                    for w in range(2):
                        xc = []
                        yc = []
                        if l%2==0:
                            xc.append(i)
                        else:
                            yc.append(i)
                        if p%2==0:
                            xc.append(j)
                        else:
                            yc.append(j)
                        if w%2==0:
                            xc.append(k)
                        else:
                            yc.append(k)
                        for y in range(len(points)):
                            if points[y][0] not in yc and points[y][1] not in xc:
                                break
                        else:
                            pos = True
print(int(pos))