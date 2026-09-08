n,q=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(q):
    k = list(map(int,input().split()))
    a=int(k[0])
    b=k[1]
    if a==1:
        print(arr[b-1])
    elif a==2:
        if b not in arr:
            print(0)
        else:
            print(arr.index(b)+1)
    else:
        for i in range(k[1]-1,k[2]):
            print(arr[i],end=' ')
        print()            
