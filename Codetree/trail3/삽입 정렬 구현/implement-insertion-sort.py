def insert_sort(arr):
    for i in range(1,len(arr)):
        j = i-1
        key = arr[i]
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

n = int(input())
arr = list(map(int, input().split()))
for i in insert_sort(arr):
    print(i,end=' ')