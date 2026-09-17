n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(n,arr):
    if n==1:
        return arr[0]
    last_gbs = f(n-1,arr)
    if last_gbs % arr[n-1] == 0:
        return last_gbs
    elif arr[n-1] % last_gbs == 0:
        return arr[n-1]
    else:
        target = arr[n-1]
        gbs = last_gbs
        for i in range(1,n):
            for i in range(2,gbs):
                if gbs%i==0 and target%i==0:
                    gbs//=i
                    target//=i
        return last_gbs * target
        
print(f(n,arr))