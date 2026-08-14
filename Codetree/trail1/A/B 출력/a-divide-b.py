a,b=map(int,input().split())
print(a//b,'.',sep='',end='')
for i in range (20):
    a=10*(a%b)
    print(a//b,end='')