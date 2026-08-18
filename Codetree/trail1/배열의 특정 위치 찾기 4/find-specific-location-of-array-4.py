arr=list(map(int,input().split()))
arr2=[]
for i in arr:
    if i==0:
        break
    if i%2==0:
        arr2.append(i)
    
sum = sum(arr2)
print(len(arr2),sum)