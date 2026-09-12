a = input()
arr = list(a)
b = input()
exist = False
for i in range(len(a)):
    k = arr.pop(-1)
    a = ''.join(arr)
    a = k + a
    arr = list(a)
    if a == b:
        exist = True
        index = i+1
if exist:
    print(index)
else:
    print(-1)