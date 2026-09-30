import sys
n = int(input())
arr = list(map(int,input().split()))
min_dis = sys.maxsize
for i in range(n):
    dis = 0
    for j in range(n):
        dis+=abs(i-j)*arr[j]
    min_dis = min(min_dis, dis)

print(min_dis)