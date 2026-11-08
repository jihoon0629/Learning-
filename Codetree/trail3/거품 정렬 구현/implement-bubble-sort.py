def bubble_sort(arr):
    sorted_list = False
    while sorted_list != True:
        sorted_list = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted_list = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

n = int(input())
arr = list(map(int, input().split()))

for i in bubble_sort(arr):
    print(i,end=' ')