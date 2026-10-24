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
    plus_prod = 1
    arr2 = arr[:]
    for i in range(3):
        plus_prod *= arr2.pop(arr2.index(max(arr2)))
    possible_max.append(plus_prod)

if minus >= 2 and plus >= 1:
    arr2 = arr[:]
    minus_prod = 1
    for i in range(2):
        minus_prod *= arr2.pop(arr2.index(min(arr2)))
    possible_max.append(minus_prod * max(arr))

if plus == 0 and zero:
    possible_max.append(0)
else:
    arr2 = arr[:]
    neg_prod = 1
    for i in range(3):
        neg_prod *= arr2.pop(arr2.index(max(arr2)))
    possible_max.append(neg_prod)

print(max(possible_max))