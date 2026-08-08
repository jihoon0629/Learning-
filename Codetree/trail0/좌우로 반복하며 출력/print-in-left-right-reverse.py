n = int(input())

a = [list(i+1 for i in range(n)) for _ in range(n)]

for i in range(n):
    if i%2==0:
        for j in range(n):
            print(a[i][j],end='')
        print()
    else:
        for j in range(n-1,-1,-1):
            print(a[i][j],end='')
        print()