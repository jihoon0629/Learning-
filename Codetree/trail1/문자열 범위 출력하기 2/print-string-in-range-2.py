a = input()
n = int(input())
a = a[::-1]
if n<len(a):
    for i in range(n):
        print(a[i], end='')
else:
    print(a)