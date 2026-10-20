a = list(map(int, input().split()))
if a[2] - a[0] == 2:
    print(0)
else:
    print(max(a[2] - a[1]-1, a[1] - a[0]-1))