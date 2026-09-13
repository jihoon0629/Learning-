n, m = map(int, input().split())

# Please write your code here.
def f(n, m):
    if n <= m:
        val = n
        g = n
    else:
        val = m
        g = m
    while True:
        if val % n == 0 and val % m == 0:
            print(val)
            break
        else:
            val += g
        
f(n,m)