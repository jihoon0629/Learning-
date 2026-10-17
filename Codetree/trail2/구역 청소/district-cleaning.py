a, b = map(int, input().split())
c, d = map(int, input().split())
cnt = 0
for i in range(101):
    if (i>=a and i<b) or (i>=c and i<d):
        cnt+=1
print(cnt)