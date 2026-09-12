a = list(input())
arr = []
for elem in a:
    if elem.isalpha():
        if ord(elem) >= ord('a') and ord(elem) <= ord('z'):
            arr.append(chr(ord(elem) - ord('a') + ord('A')))
        else:
            arr.append(elem)

arr = ''.join(arr)
print(arr)
