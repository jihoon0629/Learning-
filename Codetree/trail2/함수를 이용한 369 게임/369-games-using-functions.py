a, b = map(int, input().split())

# Please write your code here.
def tsn(n):
    arr = ['3','6','9']
    n = list(str(n))
    w = False
    for i in range(len(n)):
        if n[i] in arr:
            w = True
    if w:
        return True
    else:
        return False

cnt = 0

for i in range(a,b+1):
    if tsn(i) or i%3==0:
        cnt+=1
print(cnt)