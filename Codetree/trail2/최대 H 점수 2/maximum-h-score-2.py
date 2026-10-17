n, l = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = []
for h in range(101):
    possible_plus = l
    cnt = 0
    for j in range(n):
        if arr[j] >= h:
            cnt+=1
    if arr.count(h-1) >= l:
        cnt+=l
    else:
        cnt+=arr.count(h-1)
    if cnt >= h:
        new_arr.append(h)
print(max(new_arr))