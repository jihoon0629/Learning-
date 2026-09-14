Y, M, D = map(int, input().split())

# Please write your code here.
def yoon(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def season(m):
    if m in [3,4,5]:
        return 'Spring'
    elif m in [6,7,8]:
        return 'Summer'
    elif m in [9,10,11]:
        return 'Fall'
    else:
        return 'Winter'

def day_exist(y,m,d):
    if m in [1,3,5,7,8,10,12] and d <= 31:
        return True
    elif m in [4,6,9,11] and d <= 30:
        return True
    elif m == 2 and yoon(y) and d<=29:
        return True
    elif m == 2 and d<=28:
        return True
    else:
        return False

if day_exist(Y,M,D):
    print(season(M))
else:
    print(-1)