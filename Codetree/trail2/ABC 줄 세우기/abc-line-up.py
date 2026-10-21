n = int(input())
arr = list(input().split())
cnt = 0
for i in range(n):
    if arr[0] == chr(i+ord('A')):
        arr.pop(0)
    else:
        idx = arr.index(chr(i+ord('A')))
        cnt += idx
        arr.pop(idx)
print(cnt)