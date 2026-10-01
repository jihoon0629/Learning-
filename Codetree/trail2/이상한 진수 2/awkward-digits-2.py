def two_to_ten(n):
    sum = 0
    for i in range(len(n)):
        sum*=2
        sum+=int(n[i])
    return sum

def change(i):
    change_n = n[:]
    if n[i] == '0':
        change_n[i] = '1'
    else:
        change_n[i] = '0'
    change_n = ''.join(change_n)
    return change_n

n = list(input())

max_num = 0

for i in range(len(n)):
    changing_n = change(i)
    max_num = max(max_num, two_to_ten(changing_n))

print(max_num)