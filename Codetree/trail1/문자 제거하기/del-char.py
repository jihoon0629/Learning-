a=list(input())
while True:
    
    n=int(input())
    if n>len(a)-1:
        a.pop(-1)
    else:
        a.pop(n)
    print(''.join(a))
    if len(a)==1:
        break