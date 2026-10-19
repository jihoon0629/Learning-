import sys

def dis(x):
    for i in range(x+1,n):
        if arr[i] == 0:
            continue
        else:
            return i-x

#가장 먼 거리를 구하고 가운데 하나 채운 뒤 가장 짧은 거리 탐색

n = int(input())
arr = input()
arr = list(arr)
arr = list(map(int,arr))
max_dis = 0
min_dis = sys.maxsize
for i in range(n):
    if arr[i] == 1 and i != n-1:
        distance = dis(i)
        if max_dis < distance:
            max_dis_start = i
            max_dis = max(max_dis, distance)
arr[max_dis_start + max_dis//2] = 1
for i in range(n):
    if arr[i] == 1 and i != n-1:
        distance = dis(i)
        min_dis = min(min_dis, distance)
print(min_dis)