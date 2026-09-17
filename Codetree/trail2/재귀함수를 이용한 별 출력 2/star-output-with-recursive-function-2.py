n = int(input())

# Please write your code here.
def f(n):
    if n==0:
        return
    g(n)
    f(n-1)
    g(n)

def g(n):
    for i in range(n):
        print('*',end=' ')
    print()

f(n)