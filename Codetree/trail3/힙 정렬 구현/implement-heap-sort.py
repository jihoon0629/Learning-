def heapify(arr,n,i):
    largest = i
    x = i*2
    y = i*2+1
    if x<=n and arr[x] > arr[largest]:
        largest = x
    if y<=n and arr[y] > arr[largest]:
        largest = y
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def heap_sort(arr, n):
    for i in range(n//2,0,-1):
        heapify(arr,n,i)
    for i in range(n,0,-1):
        arr[1],arr[i] = arr[i],arr[1]
        heapify(arr,i-1,1)

n = int(input())
arr = [0] + list(map(int, input().split()))
heap_sort(arr,n)
for i in range(1,n+1):
    print(arr[i],end=' ')
