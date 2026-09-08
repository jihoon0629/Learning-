n = int(input())
a = list(map(int, input().split()))
r=[]
# Please write your code here.
while len(a)>0:
    k=a.index(max(a))
    r.append(k+1)
    a=a[:k]
    
for i in range(len(r)):
    print(r[i],end=' ')