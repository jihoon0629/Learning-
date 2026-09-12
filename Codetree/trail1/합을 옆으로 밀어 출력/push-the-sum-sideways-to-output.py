n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
sum = str(sum)
sum = sum[1:] + sum[0]
print(sum)