class Stack:
    def __init__(self):
        self.items = []

    def push(self, a):
        self.items.append(a)

    def pop(self):
        if len(self.items) == 0:
            raise Exception()
        return self.items.pop()

    def empty(self):
        return not self.items

str = input()
s = Stack()
good = True

for i in range(len(str)):
    if str[i] == '(':
        s.push(str[i])
    else:
        if s.empty():
            print('No')
            good = False
            break
        else:
            s.pop()
if s.empty() and good:
    print('Yes')
elif good and not s.empty():
    print('No')