import sys
n = int(input())
arr = list(map(int, input().split()))
min_score = sys.maxsize
for i in range(n):
    arr[i]*=2
    for j in range(n):
        score = 0
        new_arr = [elem for k, elem in enumerate(arr) if k!=j]
        for k in range(len(new_arr)-1):
            score += abs(new_arr[k] - new_arr[k+1])
        min_score = min(min_score, score)
    arr[i]//=2
print(min_score)