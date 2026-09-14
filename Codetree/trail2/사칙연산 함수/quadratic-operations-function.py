a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def f(a, o, c):
    if o not in ['+', '-', '/', '*']:
        return print('False')
    if o == '+':
        print(f'{a} + {c} = {a+c}')
    elif o == '-':
        print('%d - %d = %d'%(a,c,a-c))
    elif o == '/':
        print('%d / %d = %d'%(a,c,a//c))
    else:
        print('%d * %d = %d'%(a,c,a*c))

f(a,o,c)