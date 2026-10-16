nums = list(map(int, input().split()))
for a in range(38):
    for b in range(a,38):
        for c in range(b,38):
            for d in range(c,38):
                arr = [a,b,c,d,a+b,a+c,a+d,b+c,b+d,c+d,a+b+c,a+b+d,a+c+d,b+c+d,a+b+c+d]
                if sorted(arr) == sorted(nums):
                    print(a,b,c,d)