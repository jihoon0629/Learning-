cnt=1
n=int(input())
for i in range(n):
    for j in range(n):
        if cnt==5:
            cnt=1
        print(cnt*2,end=' ')
        cnt+=1
    print()