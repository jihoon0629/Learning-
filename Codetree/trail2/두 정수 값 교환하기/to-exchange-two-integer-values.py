n, m = map(int, input().split())

# Please write your code here.
def f(n,m):
    n,m = m,n
    return n,m

n,m = f(n,m)
print(n,m)