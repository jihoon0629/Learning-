n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
arr = []
for elem in str:
    same = True
    for i in range(len(t)):
        if t[i] != elem[i]:
            same = False
            break
    if same:
        arr.append(elem)
arr = sorted(arr)
print(arr[k-1])