A = input()
B = input()
arr = list(A)
arr2 = list(B)
# Please write your code here.
while True:
    bubun = False
    if B not in A:
        print(A)
        break
    for i in range(len(arr)-len(arr2)+1):
        if arr[i] == arr2[0]:
            silmari = True
            for j in range(len(arr2)):
                if arr[i+j] != arr2[j]:
                    silmari = False
            if silmari:
                bubun = True
                break
    if bubun:
        for k in range(len(arr2)):
            arr.pop(i)
        A = ''.join(arr)
