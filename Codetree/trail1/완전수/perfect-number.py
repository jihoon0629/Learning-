a,b=map(int,input().split())
cntwan=0
for i in range(a,b+1):
    cnt=0
    for j in range(1,i):
        if i%j==0:
            cnt+=j
    if cnt==i:
        cntwan+=1
print(cntwan)