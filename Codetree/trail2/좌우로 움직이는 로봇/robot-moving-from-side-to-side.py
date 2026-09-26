def move(time, direction, arr):
    for i in range(time):
        if direction == 'R':
            arr.append(arr[-1]+1)
        else:
            arr.append(arr[-1]-1)

def append(arr, n):
    for i in range(n):
        a,b = input().split()
        a = int(a)
        move(a,b,arr)

n,m = map(int,input().split())
a_move = [0]
b_move = [0]
append(a_move,n)
append(b_move,m)
cnt = 0
if len(a_move) < len(b_move):
    for i in range(len(b_move) - len(a_move)):
        a_move.append(a_move[-1])
else:
    for i in range(len(a_move) - len(b_move)):
        b_move.append(b_move[-1])
    
for i in range(len(a_move)):
    if i==0:
        continue
    else:
        if a_move[i] == b_move[i] and a_move[i-1] != b_move[i-1]:
            cnt+=1
print(cnt)