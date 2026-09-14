M, D = map(int, input().split())

# Please write your code here.
def day_exist(m):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m == 2:
        return 28



if M>12:
    print('No')
elif D > day_exist(M):
    print('No')
else:
    print('Yes')