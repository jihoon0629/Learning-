n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def f(a,b,i):
    while True:
        k = True
        if i+len(b) > len(a):
                return False
        for index in range(len(b)):
            if a[i+index] != b[index]:
                k = False
        return k

if len(b) > len(a):
    t = False

for i in range(len(a)-len(b)+1):
    t = False
    if f(a,b,i):
        t = True
        print('Yes')
        break
    else:
        continue
if t == False:
    print('No')