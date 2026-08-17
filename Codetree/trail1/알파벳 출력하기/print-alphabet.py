n=int(input())
cnt=ord('A')
for i in range(n):
    for j in range(i+1):
        print(chr(cnt),end='')
        if cnt==ord('Z'):
            cnt=ord('A')
        else:
            cnt+=1
    print()