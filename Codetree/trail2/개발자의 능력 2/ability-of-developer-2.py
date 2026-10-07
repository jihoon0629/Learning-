import sys
arr = list(map(int, input().split()))
min_diff = sys.maxsize
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        team_a = arr[i] + arr[j]
        for k in range(len(arr)):
            for l in range(k+1,len(arr)):
                if k not in [i,j] and l not in [i,j]:
                    team_b = arr[k] + arr[l]
                    team_c = sum(arr) - team_a - team_b
                    arr2 = [team_a, team_b, team_c]
                    arr2.sort()
                    min_diff = min(min_diff, arr2[2]-arr2[0])
print(min_diff)