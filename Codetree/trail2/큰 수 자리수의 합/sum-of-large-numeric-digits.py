a, b, c = map(int, input().split())

# Please write your code here.
def f(a,b,c):
    return a*b*c

def g(n):
    if n<10:
        return n
    return g(n//10) + n%10


print(g(f(a,b,c)))