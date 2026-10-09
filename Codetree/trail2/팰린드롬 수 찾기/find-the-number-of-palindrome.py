X, Y = map(int, input().split())
cnt = 0
for i in range(X,Y+1):
    arr = list(str(i))
    arr = arr[::-1]
    new_i = ''.join(arr)
    if int(new_i) == i:
        cnt += 1
print(cnt)