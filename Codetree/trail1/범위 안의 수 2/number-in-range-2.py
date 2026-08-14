cnt=0
count=0
for i in range(10):
    a=int(input())
    if 0<=a<=200:
        count+=a
        cnt+=1
print("%d %.1f" %(count,count/cnt))