text = input()
pattern = input()

# Please write your code here.
def f(n):
    arr = list(text)
    arr2 = list(pattern)
    cont = True
    for i in range(len(arr2)):
        if arr[n+i] != arr2[i]:
            cont = False
    return cont

con = False
for k in range(len(text) - len(pattern) + 1):
    if f(k):
        con = True
        print(k)
        break
if not con:
    print(-1)