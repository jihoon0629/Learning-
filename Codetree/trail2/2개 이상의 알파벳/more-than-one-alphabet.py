A = input()

# Please write your code here.
def f(a):
    arr = list(a)
    bool = False
    for i in range(len(arr)):
        if arr[0] != arr[i]:
            bool = True
    return bool

if f(A):
    print('Yes')
else:
    print('No')