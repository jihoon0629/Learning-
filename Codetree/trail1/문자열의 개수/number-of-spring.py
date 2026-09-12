arr = []
cnt = 0
index = 0
while True:
    a = input()
    if a == '0':
        break
    else:
        if index % 2 == 0:
            arr.append(a)            
    index+=1

print(index)
for elem in arr:
    print(elem)