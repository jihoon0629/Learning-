n=int(input())
cnt=0
while True:
    if n<=1:
        print(cnt)
        break
    cnt+=1
    n//=cnt

