n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]

c = [[0 if a[i][j] == b[i][j] else 1 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        print(c[i][j],end=' ')
    print()