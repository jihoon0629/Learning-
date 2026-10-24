def max_arr(a,b,c):
    if a>b and a>c:
        return 'A'
    elif b>a and b>c:
        return 'B'
    elif c>a and c>b:
        return 'C'
    elif a==b and a>c:
        return 'AB'
    elif b==c and b>a:
        return 'BC'
    elif c==a and c>b:
        return 'AC'
    else:
        return 'ABC'

n = int(input())
a,b,c = 0,0,0
man, point = [], []
arr = ['ABC']
cnt = 0

for _ in range(n):
    ci, si = input().split()
    man.append(ci)
    point.append(int(si))

for i in range(n):
    if man[i] == 'A':
        a += point[i]
    elif man[i] == 'B':
        b += point[i]
    else:
        c += point[i]
    arr.append(max_arr(a,b,c))

for i in range(1,len(arr)):
    if arr[i] != arr[i-1]:
        cnt += 1

print(cnt)