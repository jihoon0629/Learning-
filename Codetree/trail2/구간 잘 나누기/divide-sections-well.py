n, m = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = []
for i in range(max(arr),sum(arr)+1):
    max_m = 0
    m_count = 0
    m_sum = 0
    cnt = 0
    while True:
        m_sum += arr[cnt]
        if (cnt < n-1 and m_sum + arr[cnt+1] > i) or m-m_count == n-cnt and cnt != n-1:
            m_count+=1
            max_m = max(max_m, m_sum)
            m_sum = 0
        cnt+=1
        if cnt == n:
            m_count+=1
            max_m = max(max_m, m_sum)
            break
    if m_count == m:
        new_arr.append(max_m)
print(min(new_arr))