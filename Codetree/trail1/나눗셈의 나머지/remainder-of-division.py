arr=[0]*10
a,b=map(int,input().split())
while True:
    if a>1:
        arr[a%b]+=1
        a//=b
    else:
        break

arr2 = [i**2 for i in arr]
print(sum(arr2))