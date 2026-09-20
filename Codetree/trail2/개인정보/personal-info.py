class Man():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)

n = 5
arr = []

for i in range(n):
    name, height, weight = input().split()
    arr.append(Man(name, height, weight))

arr.sort(key = lambda x: x.name)
print('name')
for i in arr:
    print(i.name, i.height, i.weight)
print()
arr.sort(key = lambda x: -x.height)
print('height')
for i in arr:
    print(i.name, i.height, i.weight)
