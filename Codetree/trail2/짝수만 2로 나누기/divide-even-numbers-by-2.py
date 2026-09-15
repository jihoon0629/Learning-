n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(n):
    if n%2==0:
        return n//2
    else:
        return n

for i in range(n):
    arr[i] = f(arr[i])
    print(arr[i],end=' ')

