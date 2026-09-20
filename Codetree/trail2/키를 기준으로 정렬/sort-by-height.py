n = int(input())
inf = []

class man():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
for i in range(n):
    inf.append(input().split())
    inf[i][1] = int(inf[i][1])
    inf[i][2] = int(inf[i][2])
arr = [man(name, height, weight) for name, height, weight in inf]
arr.sort(key = lambda x: x.height)
for i in range(n):
    print(f"{arr[i].name} {arr[i].height} {arr[i].weight}")