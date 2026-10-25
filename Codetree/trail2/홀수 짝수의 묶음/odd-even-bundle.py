N = int(input())
arr = list(map(int, input().split()))
even = 0
odd = 0
mook = 0
now_even = True
for i in range(N):
    if arr[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    print(odd * 2 + 1)
elif even == odd:
    print(odd * 2)
elif odd > even and (odd - even) % 3 == 1:
    print(even * 2 + ((odd - even) // 3) * 2 - 1)
elif odd > even and (odd - even) % 3 == 2:
    print(even * 2 + ((odd - even) // 3) * 2 + 1 )
elif odd > even and (odd - even) % 3 == 0:
    print(even * 2 + ((odd - even) // 3) * 2)