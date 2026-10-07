n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)
cnt = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i==j or i==k or j==k:
                continue
            for g in range(n):
                first_num = int(a[g]//100==i) + int((a[g]//10)%10==j) + int(a[g]%10==k)
                if first_num == b[g]:
                    arr = [int(a[g]//100),int((a[g]//10)%10),int(a[g]%10)]
                    if int(i in arr) + int(j in arr) + int(k in arr) - b[g] == c[g]:
                        
                        continue
                    else:
                        break
                else:
                    break
            else:
                cnt+=1
print(cnt)