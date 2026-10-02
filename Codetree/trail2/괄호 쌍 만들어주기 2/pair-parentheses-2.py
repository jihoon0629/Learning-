a = input()
cnt = 0
for i in range(1,len(a)):
    if a[i] == '(' and a[i-1] == '(':
        for j in range(i+1,len(a)):
            if a[j] == ')' and a[j-1] == ')':
                cnt+=1
print(cnt)