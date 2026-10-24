arr = [list(input()) for _ in range(10)]
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'B':
            b = i,j
        elif arr[i][j] == 'R':
            r = i,j
        elif arr[i][j] == 'L':
            l = i,j
arr_y = [l[0],b[0],r[0]]
arr_x = [l[1],b[1],r[1]]
if (l[0] == b[0] == r[0] and (max(arr_x) != r[1] and min(arr_x) != r[1])) or (l[1] == b[1] == r[1] and (max(arr_y) != r[0] and min(arr_y) != r[0])):
    print(abs(l[1] - b[1]) + abs(l[0] - b[0]) + 1)
else:
    print(abs(l[0] - b[0]) + abs(l[1] - b[1]) - 1)