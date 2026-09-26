arr = [[0 for _ in range(2001)] for _ in range(2001)]
for i in range(1,4):
    a,b,c,d = map(int,input().split())
    a+=1000
    b+=1000
    c+=1000
    d+=1000
    for j in range(2001):
        for k in range(2001):
            if j>=a and j< c:
                if k>=b and k < d:
                    arr[j][k] = i
cnt = 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] in [1,2]:
            cnt+=1
print(cnt)