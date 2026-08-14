a,b=map(int,input().split())
x=1
for i in range(1,b+1):
    if i%a==0:
        x*=i
print(x)