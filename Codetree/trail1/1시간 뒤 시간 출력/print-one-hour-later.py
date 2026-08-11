h,m = map(int,input().split(":"))
if h==23:
    h=00
else:
    h+=1
print("%d:%d" %(h,m))