a = input()
b = list(a)
b[1] = 'a'
b[-2] = 'a'
c = ''.join(b)
print(c)