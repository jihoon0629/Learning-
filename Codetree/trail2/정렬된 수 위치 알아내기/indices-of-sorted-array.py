class num:
    def __init__(self, i, num=0):
        self.i = int(i)
        self.num = int(num)

n = int(input())
arr = list(map(int,input().split()))
arr2 = sorted(arr)
for elem in arr:
    print(arr2.index(elem)+1,end=' ')
    arr2[arr2.index(elem)] = -1