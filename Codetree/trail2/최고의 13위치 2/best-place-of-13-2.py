def arr_sum(x,y):
    return arr[x][y] + arr[x][y+1] + arr[x][y+2]

def pandan(x,y,x2,y2):
    if x!=x2:
        return True
    else:
        if y+2<y2:
            return True
        else:
            return False

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
max_sum = -1
for i in range(n):
    for j in range(n-2):
        for i2 in range(n):
            for j2 in range(n-2):
                if pandan(i,j,i2,j2):
                    max_sum = max(max_sum, arr_sum(i,j) + arr_sum(i2,j2))
print(max_sum)