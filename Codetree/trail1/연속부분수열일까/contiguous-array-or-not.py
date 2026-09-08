a,b=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
for i in range(a):
    if a-i<b:
            print('No')
            break
    cnt=True
    for j in range(b):        
        if arr1[i+j]!=arr2[j]:
            cnt=False            
    if cnt:
        print('Yes')
        break
    else:
        if i+j==a-1:
            print('No')
            break