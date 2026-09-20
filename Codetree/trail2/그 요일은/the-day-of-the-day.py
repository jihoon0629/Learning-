m1, d1, m2, d2 = map(int, input().split())
A = input()
arr = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
def cal(m, d):
    for i in range(1,m):
        if i==2:
            d+=29
        elif i in [1,3,5,7,8,10,12]:
            d+=31
        else:
            d+=30
    return d

day = cal(m2,d2) - cal(m1,d1)
if (arr.index(A) <= day%7):
    print(day//7 + 1)
else:
    print(day//7)