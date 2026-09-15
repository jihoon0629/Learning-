n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i]*= -1

f(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')