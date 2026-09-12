a = list(input())
arr = []
for i in a:
    if i.isdigit() or i.isalpha():
        arr.append(i)
a = ''.join(arr)
print(a.lower())