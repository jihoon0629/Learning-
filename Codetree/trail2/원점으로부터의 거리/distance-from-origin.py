class Dot:
    def __init__(self, x, y, n):
        self.x = int(x)
        self.y = int(y)
        self.n = int(n)

num = int(input())
arr = []
for i in range(num):
    x, y = input().split()
    arr.append(Dot(x, y, i+1))

arr.sort(key = lambda x: abs(x.x) + abs(x.y))
for i in arr:
    print(i.n)