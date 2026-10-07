n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: x[0])
cnt = 0
for i in range(n):
    for j in range(n):
        if j==i:
            continue
        if arr[i][0] < arr[j][0]:
            if arr[i][1] > arr[j][1]:
                break
        else:
            if arr[i][1] < arr[j][1]:
                break
    else:
        cnt+=1


print(cnt)