n,k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
max_bomb = 0
max_bomb_num = 0
over_num = [0]
for i in range(len(arr)):
    if arr.count(arr[i]) >= 2 and arr[i] not in over_num:
        over_num.append(arr[i])
for i in over_num:
    new_arr = arr[:]
    for j in range(n):
        for l in range(j+1,n):
            if arr[j]==i and arr[l]==i and l-j<=k:
                new_arr[j] = 0
                new_arr[l] = 0
    bomb = new_arr.count(0)
    if bomb > max_bomb:
        max_bomb = bomb
        max_bomb_num = i
if max_bomb_num == 0:
    print(0)
else:
    print(max_bomb_num)