n = int(input())
arr = list(map(int,input()))
maxmin_dis = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == 0 and arr[j] == 0:
            new_arr = arr[:]
            new_arr[i] = 1
            new_arr[j] = 1
            min_dis = 10000
            dis = 1000000
            for k in range(new_arr.index(1),n):
                if new_arr[k] == 1:
                    dis+=1
                    min_dis = min(min_dis, dis)
                    dis = 0
                else:
                    dis += 1
            maxmin_dis = max(maxmin_dis, min_dis)
print(maxmin_dis)