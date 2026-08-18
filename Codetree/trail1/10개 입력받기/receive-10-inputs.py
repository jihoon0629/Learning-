arr=list(map(int,input().split()))
arr2=[]
for i in arr:
    if i==0:
        break
    else:
        arr2.append(i)
print('%d %.1f' %(sum(arr2), sum(arr2)/len(arr2)))