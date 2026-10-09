import sys
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
min_max = sys.maxsize
for i in range(0,101,2):
    for j in range(0,101,2):
        arr = [0,0,0,0]
        for k in range(n):
            if points[k][0] > j:
                if points[k][1] > i:
                    arr[1] += 1
                else:
                    arr[0] += 1
            else:
                if points[k][1] > i:
                    arr[3] += 1
                else:
                    arr[2] += 1
        min_max = min(min_max, max(arr))
print(min_max)