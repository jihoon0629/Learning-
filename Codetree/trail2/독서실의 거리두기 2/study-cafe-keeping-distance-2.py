import sys

def dis(x):
    for h in range(x+1,n):
        if arr[h] == 1:
            if x==0 and arr[x] == 0:
                return x-h
            return h-x
    return -(n-1-x)    
n = int(input())
arr = input()
arr = list(map(int,list(arr)))
max_dis = 0
max_dis_start = -1
min_dis = sys.maxsize
last_empty = -1
last_empty_start = -1
for i in range(n):
    if arr[i] == 1 or i==0:
        distance = dis(i)
        if distance < 0:
            if distance < last_empty:
                last_empty = distance
                last_empty_start = i
                continue
        if max_dis < distance:
            max_dis = distance
            max_dis_start = i
if max_dis//2 < -last_empty:
    if last_empty_start > 0:
        arr[-1] = 1
    else:
        arr[0] = 1
else:
    arr[max_dis_start+max_dis//2] = 1
for i in range(n):
    if arr[i] == 1 and i != n-1:
        distance = dis(i)
        if distance < 0:
            continue
        if min_dis > distance:
            min_dis = distance
print(min_dis)