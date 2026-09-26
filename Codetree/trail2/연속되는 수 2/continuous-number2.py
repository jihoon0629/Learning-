n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
max_cnt = 0
cnt = 0
for i in range(n):
    if i==0 or arr[i] != arr[i-1]:
        if cnt > max_cnt:
            max_cnt = cnt
        cnt=1
    elif arr[i] == arr[i-1]:
        cnt+=1
if cnt > max_cnt:
    max_cnt = cnt
print(max_cnt)