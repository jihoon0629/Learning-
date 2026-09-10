arr=[]
for i in range(10):
    a=input()
    arr.append(a)
a=input()
exist = False
for i in range(10):
    if arr[i][-1] == a:
        print(arr[i])
        exist = True
if not exist:
    print('None')