a=0
for i in range(3):
    k=input().split()
    if k[0]=='Y' and int(k[1])>=37:
        a+=1
if a>=2:
    print('E')
else:
    print('N')