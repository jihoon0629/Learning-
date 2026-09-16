n = int(input())

# Please write your code here.
def f(n):
    if n==0:
        return
    f(n-1)
    for i in range(n):
        print('*',end='')
    print()

f(n)