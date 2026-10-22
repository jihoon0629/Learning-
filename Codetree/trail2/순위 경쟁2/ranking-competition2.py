n = int(input())
c = []
s = []
for _ in range(n):
    ci, si = input().split()
    c.append(ci)
    s.append(int(si))
arr = [0,0]
honor = []
change = 0
honor.append('AB')
for i in range(n):
    if c[i] == 'A':
        arr[0] += s[i]
    else:
        arr[1] += s[i]
    if arr[0] > arr[1]:
        honor.append('A')
    elif arr[1] > arr[0]:
        honor.append('B')
    else:
        honor.append('AB')
for i in range(len(honor)-1):
    if honor[i] != honor[i+1]:
        change += 1
print(change)