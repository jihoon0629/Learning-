n=int(input())
count=0
for i in range(n):
    a=int(input())
    count+=a
print("%d %.1f" %(count,count/n))