MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append((codename, int(score)))

# Please write your code here.
lower = 100
for i in range(MAX_N):
    if users[i][1] < lower:
        lower = users[i][1]
        lower_index = i

spy = users[lower_index]
spy_name, spy_score = spy
print(spy_name, spy_score)