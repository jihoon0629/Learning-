cnt=0
cnt2=0
arr=list(map(int,input().split()))
for i in range(10):
    if i%2==0:
        cnt+=arr[i]
    else:
        cnt2+=arr[i]

if cnt>=cnt2:
    print(cnt-cnt2)
else:
    print(cnt2-cnt)