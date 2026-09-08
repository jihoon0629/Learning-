n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min = min(a)
cnt=0
for i in range(n):
    if a[i] == min:
        cnt+=1
print(min,cnt)