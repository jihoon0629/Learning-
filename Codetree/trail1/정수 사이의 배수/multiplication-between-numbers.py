a,b=map(int,input().split())
cnt=0
count=0
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        cnt+=1
        count+=i
if cnt!=0:
    print(f"{count} {count/cnt:.1f}")