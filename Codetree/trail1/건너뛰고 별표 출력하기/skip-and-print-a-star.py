n=int(input())
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()
    print()
for j in range(n-1,0,-1):
    for k in range(j):
        print('*',end='')
    print()
    print()