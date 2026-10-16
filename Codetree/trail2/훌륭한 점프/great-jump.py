def is_possible(a):
    new_arr = []
    for i, elem in enumerate(arr):
        if elem <= a:
            new_arr.append(i)
    for i in range(1,len(new_arr)):
        if new_arr[i] - new_arr[i-1] > k:
            return False
    return True

n, k = map(int, input().split())
arr = list(map(int, input().split()))
minmin = []
for i in range(max(arr[0], arr[-1]),101):
    if is_possible(i):
        minmin.append(i)
print(min(minmin))