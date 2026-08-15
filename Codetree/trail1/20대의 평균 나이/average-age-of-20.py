cnt=0
count=0
while True:
    a=int(input())
    if a//10!=2:
        break
    else:
        count+=a
        cnt+=1
print("%.2f" %(count/cnt))