class student():
    def __init__(self, n, k, e, m):
        self.n = n
        self.k = int(k)
        self.e = int(e)
        self.m = int(m)

n = int(input())
arr = []
for i in range(n):
    n,k,e,m = input().split()
    arr.append(student(n,k,e,m))
arr.sort(key = lambda x: x.k + x.e + x.m)
for i in arr:
    print(i.n,i.k,i.e,i.m)