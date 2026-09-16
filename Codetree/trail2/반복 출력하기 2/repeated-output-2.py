n = int(input())

# Please write your code here.
def f(n):
    if n==0:
        return
    else:
        f(n-1)
        print('HelloWorld')

f(n)