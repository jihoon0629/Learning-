n = int(input())
l = []
r = []
arr = [0 for _ in range(101)]
cnt = 0
for _ in range(n):
    left, right = map(int, input().split())
    l.append(left)
    r.append(right)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            arr2 = arr[:]
            for line in range(n):
                if line == i or line == j or line == k:
                    continue
                for o in range(l[line], r[line]+1):
                    arr2[o]+=1
            for ver in range(101):
                if arr2[ver]>1:
                    break
            else:
                cnt+=1
print(cnt)