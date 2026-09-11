cnt = 0
a = input()
b = input()
for i in range(len(a)-len(b)+1):
    o = True
    for j in range(len(b)):
        if a[i+j] != b[j]:
            o = False
            break
    if o == True:
        cnt+=1
print(cnt)
        
        