n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)
for x in range(1,5001):
    for j in range(1,n+1):
        if a[j-1]<= x*2**j <= b[j-1]:
            continue
        else:
            break
    else:
        print(x)
        break