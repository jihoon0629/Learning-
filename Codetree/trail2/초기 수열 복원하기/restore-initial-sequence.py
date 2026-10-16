n = int(input())
adjacent = list(map(int, input().split())) if n >= 2 else []
for i in range(1,n+1):
    arr = [i]
    for j in range(len(adjacent)):
        arr.append(adjacent[j]-arr[j])
    for i in range(len(arr)):
        if arr[i] <= 0:
            break
    else:
        if len(set(arr)) == n:
            for j in arr:
                print(j,end=' ')
            break