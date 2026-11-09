def radix_sort(arr):
    for i in range(1,len(str(max(arr)))+1):
        new_arr = [[] for _ in range(10)]
        for j in arr:
            if len(str(j)) < i:
                new_arr[0].append(j)
            else:
                new_arr[int(str(j)[-i])].append(j)
        store_arr = []
        for i in range(10):
            for j in range(len(new_arr[i])):
                store_arr.append(new_arr[i][j])
        arr = store_arr
    return arr

n = int(input())
arr = list(map(int, input().split()))
for i in radix_sort(arr):
    print(i,end=' ')