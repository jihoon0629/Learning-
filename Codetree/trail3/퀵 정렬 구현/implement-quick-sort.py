def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] < pivot:
            i+=1
            arr_swap(i,j)
    arr_swap(i+1,high)
    return i+1

def quick_sort(arr,low,high):
    if low<high:
        pos  = partition(arr,low,high)
        quick_sort(arr,low,pos-1)
        quick_sort(arr,pos+1,high)
    return arr

def arr_swap(i,j):
    arr[i],arr[j] = arr[j],arr[i]


n = int(input())
arr = list(map(int, input().split()))
for i in quick_sort(arr,0,len(arr)-1):
    print(i,end=' ')