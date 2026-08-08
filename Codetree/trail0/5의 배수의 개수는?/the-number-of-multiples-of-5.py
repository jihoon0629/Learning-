total = 0
a = [list(map(int,input().split())) for _ in range(4)]

for i in range(4):
    for j in range(4):
        if a[i][j] % 5 == 0:
            total +=1
print(total)