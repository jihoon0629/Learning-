arr=[]
for i in range(2):
    arr.append(list(map(int,input().split())))
    print(f'{sum(arr[i])/4:.1f}',end=' ')
print()
for i in range(4):
    print(f'{(arr[0][i]+arr[1][i])/2:.1f}',end=' ')
print()
sum=0
for i in range(2):
    for j in range(4):
        sum+=arr[i][j]
     
print(f'{sum/8:.1f}')