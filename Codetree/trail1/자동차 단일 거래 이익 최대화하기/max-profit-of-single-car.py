n = int(input())
price = list(map(int, input().split()))
max=0
# Please write your code here.
for i in range(n):
    for j in range(i+1,n):
        if max<price[j]-price[i]:
            max=price[j]-price[i]
print(max)