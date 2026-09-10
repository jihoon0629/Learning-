n = int(input())
arr = input().split()
a = ''.join(arr)
cnt = 1
while cnt <= len(a):
    if cnt%5==0:
        print(a[cnt-1])
        cnt+=1
    else:
        print(a[cnt-1],end='')
        cnt+=1