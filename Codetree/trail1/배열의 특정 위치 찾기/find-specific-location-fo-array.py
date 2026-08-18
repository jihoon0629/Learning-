cnt2=0
sum3=0
arr=list(map(int,input().split()))
for i in range(10):
    if (i+1)%2==0:
        cnt2+=arr[i]
    if (i+1)%3==0:
        sum3+=arr[i]
print('%d %.1f' %(cnt2,sum3/3))