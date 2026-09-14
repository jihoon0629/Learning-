a, b = map(int, input().split())

# Please write your code here.
def prime(n):
    prime = True
    for i in range(2,n):
        if n%i==0:
            prime = False
    return prime

cnt = 0
for i in range(a, b+1):
    if prime(i):
        cnt+=i
print(cnt)