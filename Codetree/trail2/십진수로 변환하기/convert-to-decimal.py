binary = input()
num = 0
index = 0
while True:
    if index == len(binary):
        break
    num = num*2 + int(binary[index])
    index+=1
    
print(num)