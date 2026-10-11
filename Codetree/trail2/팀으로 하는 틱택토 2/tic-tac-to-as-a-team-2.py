def team_win(l):
    if len(set(l)) == 2:
        win_team.append(tuple(sorted(set(l))))

win_team = []
cnt = 0
arr = [list(map(int,input())) for _ in range(3)]
for i in range(3):
    arr2 = arr[:]
    team_win(arr2[i])
for i in range(3):
    arr2 = []
    for j in range(3):
        arr2.append(arr[j][i])
    team_win(arr2)
for i in range(2):
    arr2 = []
    for j in range(3):
        if i%2==0:
            arr2.append(arr[j][j])
        else:
            arr2.append(arr[j][2-j])
    team_win(arr2)
print(len(set(win_team)))