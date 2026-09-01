arr=list(map(int,input().split()))
check=[0]*10
cnt=0
while True:
    if arr[cnt]==0:
        for i in range(10,0,-1):
            print(f"{i}0 - {check[i-1]}")
        break
    elif arr[cnt]<10:
        cnt+=1
        continue
    else:
        check[(arr[cnt]//10)-1]+=1
        cnt+=1