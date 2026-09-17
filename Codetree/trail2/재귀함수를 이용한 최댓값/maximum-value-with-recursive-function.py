n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(arr,n):
    if n==1:
        return arr[0]
    before_max = f(arr,n-1)
    if before_max >= arr[n-1]:
        return before_max
    else:
        return arr[n-1]

print(f(arr,n))
