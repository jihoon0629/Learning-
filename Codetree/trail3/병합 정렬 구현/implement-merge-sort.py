def merge_sort(arr,low,high):
    mid = (low + high) // 2
    if low < high:
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    i = low
    j = mid + 1
    k = low
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged_arr[k] = arr[i]
            i+=1
            k+=1
        else:
            merged_arr[k] = arr[j]
            j+=1
            k+=1
    while i<=mid:
        merged_arr[k] = arr[i]
        i+=1
        k+=1
    while j<=high:
        merged_arr[k] = arr[j]
        j+=1
        k+=1
    for i in range(low,high+1):
        arr[i] = merged_arr[i]
    return arr


n = int(input())
arr = list(map(int, input().split()))
merged_arr = [-1 for _ in range(n)]
merge_sort(arr,0,len(arr)-1)
for i in merged_arr:
    print(i,end=' ')