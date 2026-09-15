n, m = map(int, input().split())
A = list(map(int, input().split()))
sum = 0
# Please write your code here.
def f(n):
    global sum
    sum += A[n-1]
    return sum

while True:
    if m == 1:
        sum += A[0]
        break
    else:
        sum = f(m)
        if m%2==0:
            m//=2
        else:
            m-=1
print(sum)