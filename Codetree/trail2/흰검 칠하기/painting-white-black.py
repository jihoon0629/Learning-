n = int(input())
arr = {}
black = {}
white = {}
cnt = 0
for i in range(n):
    a,b = input().split()
    a = int(a)
    if b == 'R':
        for j in range(cnt,cnt+a):
            black[j] = black.get(j,0) + 1
            white[j] = white.get(j,0)
            if black[j] >= 2 and white[j] >= 2:
                arr[j] = 'gray'
            else:
                arr[j] = 'black'
        cnt += (a-1)
    else:
        for j in range(cnt-a+1,cnt+1):
            black[j] = black.get(j,0)
            white[j] = white.get(j,0) + 1
            if white[j] >= 2 and black[j] >= 2:
                arr[j] = 'gray'
            else:
                arr[j] = 'white'
        cnt -= (a-1)
gray = 0
black = 0
white = 0
for i in arr.values():
    if i == 'gray':
        gray += 1
    elif i == 'black':
        black += 1
    else:
        white += 1
print(white, black, gray)