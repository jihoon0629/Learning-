T, a, b = map(int, input().split())
c = []
x = []
cnt =0
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))
for k in range(a,b+1):
    close = 1000
    close_cnt = 'N'
    for t in range(T):
        dis = abs(k - x[t])
        if close == dis:
            if c[t] == 'S':
                close_cnt = 'S'
        elif dis < close:
            close = dis
            close_cnt = c[t]
    if close_cnt == 'S':
        cnt+=1
print(cnt)