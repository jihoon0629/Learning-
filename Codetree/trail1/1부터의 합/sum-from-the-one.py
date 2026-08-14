count=0
n=int(input())
for i in range(1,101):
    count+=i
    if count>=n:
        print(i)
        break