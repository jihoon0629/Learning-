n = int(input())
arr = input()
arr = list(arr)
for i in range(n):
    new_arr = []
    for j in range(n-i+1):
        bb_arr = arr[j:j+i+1]
        new_arr.append(bb_arr)
    for j in range(len(new_arr)):
        new_arr[j] = ''.join(new_arr[j])
    if len(set(new_arr)) == n-i+1:
        print(i+1)
        break

