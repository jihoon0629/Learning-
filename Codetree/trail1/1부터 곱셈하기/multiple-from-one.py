n=int(input())
x=1
for i in range(1,11):
    x*=i
    if x>=n:
        print(i)
        break
if n>x:
    print(i)
    