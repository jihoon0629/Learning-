def compare(i):
    a = a_move[i]
    b = b_move[i]
    if i==0:
        return 0
    if a==b:
        return 3
    elif a>b:
        return 1
    else:
        return 2

def move(v, t, arr):
    for i in range(t):
        arr.append(arr[-1]+v)

a_move = [0]
b_move = [0]
n, m = map(int,input().split())
for i in range(n):
    v, t = map(int,input().split())
    move(v, t, a_move)
for i in range(m):
    v, t = map(int,input().split())
    move(v, t, b_move)

cnt = 0
front = compare(0)
for i in range(1,len(a_move)):
    if compare(i) != front:
        cnt+=1
        front = compare(i)

print(cnt)