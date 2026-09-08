n = int(input())
nums = list(map(int, input().split()))
cnt=0
# Please write your code here.
nums.sort(reverse=True)
while True:
    if cnt==(len(nums)-1) and nums.count(nums[cnt])!=1:
        print(-1)
        break
    elif nums.count(nums[cnt])>=2:
        cnt+=1
    else:
        print(nums[cnt])
        break