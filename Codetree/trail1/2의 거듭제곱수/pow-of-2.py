i=0
n=int(input())
while True:
    if n==2**i:
        print(i)
        break
    else:
        i+=1