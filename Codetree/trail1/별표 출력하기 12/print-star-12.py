n=int(input())


for j in range(1,n+1):
    print('* ',end='')
print()
for i in range(2,n+1):
    for j in range(1,n+1):
        if j%2==0 and i<=j:
            print('* ',end='')
        else:
            print(' ',end=' ')
    print()