n=int(input())
cnt=0
for i in range(n):
    arr=list(map(int,input().split()))
    if sum(arr)/4 >= 60:
        cnt+=1
        print('pass')
    else:
        print('fail')
print(cnt)