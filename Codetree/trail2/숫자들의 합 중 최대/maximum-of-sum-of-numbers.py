X, Y = map(int, input().split())
max_sum = 0
for i in range(X,Y+1):
    arr = list(map(int,list(str(i))))
    sum_arr = sum(arr)
    max_sum = max(max_sum, sum_arr)
print(max_sum)