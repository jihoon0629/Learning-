n, m = map(int, input().split())
a_move = [0]
b_move = [0]
def f(direction, length, arr):
    if direction == 'R':
        for i in range(length):
            arr.append(arr[-1]+1)
    else:
        for i in range(length):
            arr.append(arr[-1]-1)

for i in range(n):
    a,b = input().split()
    b = int(b)
    f(a,b,a_move)
for i in range(m):
    a,b = input().split()
    b = int(b)
    f(a,b,b_move)

if len(a_move) < len(b_move):
    less = len(a_move)
else:
    less = len(b_move)
exist = False
for i in range(1,less):
    if a_move[i] == b_move[i]:
        print(i)
        exist = True
        break
if not exist:
    print(-1)