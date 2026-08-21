count=0
n=int(input())
arr=[]
k=n
while True:
    arr.append(k)
    if k%5==0:
        count+=1
    if count>=2:
        break
    k+=n
for i in range(len(arr)):
    print(arr[i],end=' ')