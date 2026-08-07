a,b = map(int,input().split())

l = [a,b]

for i in range(10):
    print(l[i],end=' ')
    l.append((l[i]+l[i+1])%10)