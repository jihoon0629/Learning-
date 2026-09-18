n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    if i%2==0:
        arr2 = arr[:i+1]
        arr2 = sorted(arr2)
        print(arr2[i//2],end=' ')
