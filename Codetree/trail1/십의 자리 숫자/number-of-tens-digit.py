arr=list(map(int,input().split()))
cnt=0
count=[0]*9
while True:
    if arr[cnt]==0:
        break
    elif arr[cnt]<10:
        cnt+=1
        continue
    count[(arr[cnt]//10)-1]+=1
    cnt+=1
for i in range(9):
    print(f"{i+1} - {count[i]}")