cnt_total=0
a,b=map(int,input().split())
for i in range(a,b+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==3:
        cnt_total+=1
print(cnt_total)