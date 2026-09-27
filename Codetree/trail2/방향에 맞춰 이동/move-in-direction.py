def moving(dir, dist, arr):
    if dir == 'N':
        arr[1] += dist
    elif dir == 'S':
        arr[1] -= dist
    elif dir == 'E':
        arr[0] += dist
    else:
        arr[0] -= dist

n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]
arr = [0, 0]
for i in range(n):
    moving(dir[i], dist[i], arr)
print(arr[0],arr[1])