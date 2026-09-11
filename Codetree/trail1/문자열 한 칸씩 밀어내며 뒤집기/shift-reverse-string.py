input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
for elem in queries:
    if elem == 1:
        input_str = input_str[1:] + input_str[0]
        print(input_str)
    elif elem == 2:
        input_str = input_str[-1] + input_str[:-1]
        print(input_str)
    else:
        input_str = input_str[::-1]
        print(input_str)

