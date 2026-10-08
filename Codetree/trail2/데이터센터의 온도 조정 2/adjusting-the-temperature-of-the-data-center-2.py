N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
max_work = 0
for tem in range(-1,1002):
    work = 0
    for i in range(N):
        if ranges[i][0] <= tem <= ranges[i][1]:
            work += G
        elif ranges[i][0] > tem:
            work += C
        else:
            work += H
    max_work = max(max_work, work)
print(max_work)