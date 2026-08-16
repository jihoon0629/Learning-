n=int(input())
k=False
for i in range(2,n):
    if n%i==0:
        k=True
        break
    else:
        k=False
if k==False:
    print('N')
else:
    print('C')
