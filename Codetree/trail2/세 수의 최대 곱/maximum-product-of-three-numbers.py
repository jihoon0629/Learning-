n = int(input())
arr = list(map(int, input().split()))
possible_max = []
plus = 0
minus = 0
zero = 0 in arr

for i in range(n):
    if arr[i] > 0:
        plus += 1
    elif arr[i] < 0:
        minus += 1
    if minus >= 2 and plus >= 3:
        break

if plus >= 3:
    plus_max = 1
    arr2 = arr[:]
    for i in range(3):
        plus_max *= arr2.pop(arr2.index(max(arr2)))
    possible_max.append(plus_max)

if minus >= 2 and plus >= 1:
    arr2 = arr[:]
    minus_max = 1
    for i in range(2):
        minus_max *= arr2.pop(arr2.index(min(arr2)))
    possible_max.append(minus_max * max(arr))

if plus == 0 and zero:
    possible_max.append(0)
else:
    arr_sum = 1
    for i in range(3):
        arr_sum *= arr.pop(arr.index(max(arr)))
    possible_max.append(arr_sum)

print(max(possible_max))