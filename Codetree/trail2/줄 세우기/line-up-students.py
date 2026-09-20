class Student():
    def __init__(self, hei, wei, num):
        self.hei = int(hei)
        self.wei = int(wei)
        self.num = int(num)

n = int(input())
arr = []
for i in range(n):
    h,w = input().split()
    arr.append(Student(h,w,i+1))

arr.sort(key = lambda x: (-x.hei, -x.wei, x.num))

for i in arr:
    print(i.hei, i.wei, i.num)