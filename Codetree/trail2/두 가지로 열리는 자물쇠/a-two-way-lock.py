import sys
def length(a,b):
    min_len = sys.maxsize
    for i in range(N):
        if a > N:
            a-=N
        if a == b:
            min_len = min(min_len, i)
        a+=1
    for i in range(N):
        if a < 1:
            a+=N
        if a == b:
            min_len = min(min_len, i)
        a-=1
    return min_len



N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
cnt = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if length(i,a1)<=2 and length(j,b1) <= 2 and length(k,c1)<=2 and length(i,a2) <= 2 and length(j,b2)<=2 and length(k,c2) <= 2:
                cnt+=1

if N<5:
    print((N**3)*2-cnt)
else:
    print(250-cnt)