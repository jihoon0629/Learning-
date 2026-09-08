arr=[]
sum=0
for i in range(4):
    arr.append(list(map(int,input().split())))
for i in range(4):
    for j in range(4):
        if i>=j:
            sum+=arr[i][j]
print(sum)