class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, a):
        self.items.append(a)
    
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def empty(self):
        return int(not self.items)

    def top(self):
        if self.empty():
            raise Exception("Stack is empty")
        return self.items[-1]

N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

s = Stack()

for i in range(N):
    if command[i] == 'push':
        s.push(value[i])
    elif command[i] == 'pop':
        print(s.pop())
    elif command[i] == 'size':
        print(s.size())
    elif command[i] == 'empty':
        print(s.empty())
    elif command[i] == 'top':
        print(s.top())