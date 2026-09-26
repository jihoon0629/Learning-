def move(v, t, arr):
    for i in range(t):
        arr.append(arr[-1]+v)
n, m = map(int, input().split())
a_move = [0]
b_move = [0]
for i in range(n):
    v,t = map(int,input().split())
    move(v, t, a_move)
for i in range(m):
    v,t = map(int,input().split())
    move(v, t, b_move)
who_is_pioneer = None
cnt = 0
for i in range(1,len(a_move)):
    if a_move[i] > b_move[i]:
        if who_is_pioneer == 'b':
            cnt+=1
        who_is_pioneer = 'a'
    elif a_move[i] < b_move[i]:
        if who_is_pioneer == 'a':
            cnt+=1
        who_is_pioneer = 'b'
print(cnt)