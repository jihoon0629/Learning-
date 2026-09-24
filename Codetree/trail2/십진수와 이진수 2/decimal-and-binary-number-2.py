n = input()
sum = 0
arr=[]
for i in n:
    sum = sum*2+int(i)
sum*=17
while True:
    if sum<2:
        arr.append(sum)
        break
    arr.append(sum%2)
    sum//=2
arr = arr[::-1]
for i in arr:
    print(i,end='')