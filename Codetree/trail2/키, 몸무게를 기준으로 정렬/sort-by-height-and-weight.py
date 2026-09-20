class Man():
    def __init__(self, n, h, w):
        self.n = n
        self.h = int(h)
        self.w = int(w)

n = int(input())
arr = []
for i in range(n):
    n, h, w = input().split()
    arr.append(Man(n, h, w))
arr.sort(key = lambda x: (x.h, -x.w))
for i in arr:
    print(i.n, i.h, i.w)