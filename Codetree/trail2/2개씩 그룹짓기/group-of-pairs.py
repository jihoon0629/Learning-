n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums = sorted(nums)
arr = []
for i in range(n):
    arr.append(nums[i] + nums[2*n-i-1])

print(max(arr))