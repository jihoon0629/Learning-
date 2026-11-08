def minimum_sort(arr):
    for i in range(len(arr)-1):
        minimum = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[i],arr[minimum] = arr[minimum],arr[i]
    return arr

n = int(input())
arr = list(map(int, input().split()))
for i in minimum_sort(arr):
    print(i,end=' ')
