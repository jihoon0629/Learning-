a, b = map(int, input().split())

# Please write your code here.
def evenprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    arr = list(str(n))
    arr = list(map(int,arr))
    if sum(arr)%2==0:
        return True

cnt=0
for i in range(a,b+1):
    if evenprime(i):
        cnt+=1
print(cnt)