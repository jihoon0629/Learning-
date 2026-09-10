cnt=0
count=0
n=int(input())
for i in range(n):
    a=input()
    if a[0]=='a':
        cnt+=1
    count+=len(a)
print(count,cnt)