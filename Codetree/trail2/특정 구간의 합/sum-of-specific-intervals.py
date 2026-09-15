n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def sum(a,b):
    sum = 0
    for i in range(a,b+1):
        sum += arr[i-1]
    return sum
    
for i in range(m):
    print(sum(queries[i][0], queries[i][1]))