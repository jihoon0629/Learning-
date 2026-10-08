N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
P = [gift[0] for gift in gifts]
S = [gift[1] for gift in gifts]
max_enable_cnt = 0
for discount in range(N):
    money = B
    cnt = 0
    if money - P[discount]//2 - S[discount] >= 0:
        cnt += 1
        money = money - P[discount]//2 - S[discount]
    new_gift = []
    for l in range(N):
        new_gift.append(P[l] + S[l])
    new_gift.pop(discount)
    new_gift.sort()
    for i in range(len(new_gift)):
        if money - new_gift[i] < 0:
            break
        else:
            money -= new_gift[i]
            cnt+=1
    max_enable_cnt = max(max_enable_cnt, cnt)
print(max_enable_cnt)