n = int(input())
price = list(map(int, input().split()))
min=max(price)
# Please write your code here.
for i in range(n):
    for j in range(i+1,n):
        if min>price[j]-price[i]:
            min=price[j]-price[i]
print(min)