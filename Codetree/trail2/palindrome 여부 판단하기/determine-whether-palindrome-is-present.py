A = input()

# Please write your code here.
def f(a):
    arr = list(a)
    arr2 = arr[::-1]
    bool = True
    for i in range(len(arr)):
        if arr[i] != arr2[i]:
            bool = False
    return bool


if f(A):
    print('Yes')
else:
    print('No')