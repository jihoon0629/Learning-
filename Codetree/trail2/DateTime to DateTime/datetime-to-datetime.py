a, b, c = map(int, input().split())

def cal(a,b,c):
    b += 24 * a
    c += 60 * b
    return c

if cal(a,b,c) - cal(11,11,11) < 0:
    print(-1)
else:
    print(cal(a,b,c) - cal(11,11,11))