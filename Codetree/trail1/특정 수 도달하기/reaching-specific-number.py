sum=0
cnt=0
arr=list(map(int,input().split()))
for i in arr:
    if i>=250:
        break
    else:
        sum+=i
        cnt+=1
print("%d %.1f" %(sum,sum/cnt))