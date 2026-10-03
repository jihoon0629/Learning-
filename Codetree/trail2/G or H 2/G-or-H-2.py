n = int(input())
arr = [0 for _ in range(101)]
for i in range(n):
    a,b = input().split()
    arr[int(a)] = b

max_len = 0
for i in range(101):
    if arr[i] == 'G' or arr[i] == 'H':
        for j in range(101 - i):
            if arr[i+j] == 'G' or arr[i+j] == 'H':
                h_cnt = 0
                g_cnt = 0
                for k in range(j+1):
                    if arr[i+k] == 'G':
                        g_cnt += 1
                    elif arr[i+k] == 'H':
                        h_cnt += 1
                if g_cnt == h_cnt or h_cnt==0 or g_cnt==0:
                    max_len = max(max_len, j)
print(max_len)