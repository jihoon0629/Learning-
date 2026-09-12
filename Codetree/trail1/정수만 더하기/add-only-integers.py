a = input()
arr = list(a)
cnt=0
for i in arr:
    if i.isdigit():
        cnt+=int(i)
print(cnt)