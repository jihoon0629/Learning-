import sys
arr = list(map(int, input().split()))
min_diff = sys.maxsize
exist = False
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(j+1,len(arr)):
            if j != i and k != i:
                team_a = arr[i]
                team_b = arr[j]+arr[k]
                team_c = sum(arr) - team_a - team_b
                if team_a != team_b and team_b != team_c and team_a != team_c:
                    arr2 = [team_a,team_b,team_c]
                    arr2.sort()
                    min_diff = min(min_diff, arr2[2]-arr2[0])
                    exist = True
if exist:
    print(min_diff)
else:
    print(-1)