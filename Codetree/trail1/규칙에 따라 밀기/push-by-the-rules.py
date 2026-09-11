input_str = input()
direction = list(input())
for elem in direction:
    if elem == 'L':
        input_str = input_str[1:] + input_str[0]
    else:
        input_str = input_str[-1] + input_str[:-1]
print(input_str)