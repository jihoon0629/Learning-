sum = 0
cnt = 0
arr = []
n = int(input())
for i in range(n):
    a = input()
    arr.append(a)
alphabet = input()
for i in range(n):
    if arr[i][0] == alphabet:
        cnt += 1
        sum += len(arr[i])
print(f'{cnt} {sum/cnt:.2f}')