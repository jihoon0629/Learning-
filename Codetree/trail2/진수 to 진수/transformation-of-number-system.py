a, b = map(int, input().split())
n = input()
arr = []
sum = 0
for i in str(n):
    sum = sum*a + int(i)
while True:
    if sum < b:
        arr.append(sum)
        break
    arr.append(sum%b)
    sum//=b
arr = arr[::-1]
for i in arr:
    print(i,end='')