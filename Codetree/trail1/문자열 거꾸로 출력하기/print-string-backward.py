while True:
    a = input()
    if a == 'END':
        break
    elif a.isalpha():
        print(a[::-1])