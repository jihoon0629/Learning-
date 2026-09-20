class num:
    def __init__(self, i, num=0):
        self.i = int(i)
        self.num = int(num)

n = int(input())
arr = input().split()

for i in range(n):
    arr[i] = num(arr[i])

arr2 = arr[:]
arr2.sort(key = lambda x: x.i)
for i in range(1,n+1):
    arr2[i-1].num = i

for i in arr:
    print(i.num,end=' ')