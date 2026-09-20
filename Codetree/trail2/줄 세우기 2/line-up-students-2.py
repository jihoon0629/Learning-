class std():
    def __init__(self, h, w, n):
        self.h = int(h)
        self.w = int(w)
        self.n = int(n)

n = int(input())
arr = []
for i in range(n):
    h, w = input().split()
    arr.append(std(h, w, i+1))
arr.sort(key = lambda x: (x.h, -x.w))
for i in arr:
    print(i.h, i.w, i.n)