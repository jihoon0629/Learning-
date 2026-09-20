m1, d1, m2, d2 = map(int, input().split())

arr = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
all_day = 0
for i in range(1, m2):
    all_day+=arr[i]
for i in range(1, m1):
    all_day-=arr[i]
all_day = all_day + d2 - d1 + 1
print(all_day)