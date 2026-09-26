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


for i in range(1,len(a_move)):
    if a_move[i] == b_move[i]:
        print(i)
        break
else:
    print(-1)