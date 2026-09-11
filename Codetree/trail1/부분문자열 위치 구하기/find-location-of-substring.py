input_str = input()
target_str = input()

# Please write your code here.
intherestr = False
for i in range(len(input_str) - len(target_str) + 1):
    if input_str[i] == target_str[0]:
        inthere = True
        for j in range(len(target_str)):
            if input_str[i+j] != target_str[j]:
                inthere = False
                break
        if inthere == True:
            intherestr = True
            intherestrindex = i
            break
if intherestr:
    print(intherestrindex)
else:
    print(-1)